#!/bin/bash
#ident  "@(#)backup_freenas_rsync    0.19     2017/09/01     K. Raquel Sanborn"
#
#   Script name:
#       backup_freenas_rsync
#
#   OS supported:
#       FreeNAS 9.3, 9.10
#
#   Description:
#	Perform the following:
#	 - Create log file.
#	 - Scrub the backup media, if error found, abort backup
#	 - Backup FreeNAS file systems, via "rsync" to a local file system.
#
#   Usage:
#	sudo /bin/su -
#	zpool import Backup750
#	     Or;
#	zpool import Backup
#
#	cd ~${MY_USER_NAME}/bin
#
#	    Optionally;
#	setenv MY_BACKUP_SCRUB off
#
#	nohup ./backup_freenas_rsync >/dev/null &
#		or
#	batch -q a -f ./backup_freenas_rsync
#
#   Configuration:
#       MY_LOGDIR=/var/log/local
#	MY_SOURCE=/mnt/${MY_SOURCE_PATH}
#	
#   Author info:
#       K. Raquel Sanborn
#       (C) Copyright K. Raquel Sanborn
#
#   Permission and fees:
#       You have the right to run this script without any warranty. If you
#       find it useful, let me know, (and send cash :-). If it breaks
#       something, I am not responsible, (it has SOME builtin safe guards).
#       If you modify this script, do not alter my credits, add your own.
#
#   Notes:
#	It is assumed that the backup will fit on the destination. Thus,
#	checking log file after backup is helpful to detect errors.
#
#   History:
#       2016/03/12 - K. Raquel Sanborn - Original creation from "backup_rsync_fs"
#	2016/05/25 - K. Raquel Sanborn - Fix Rsync exclude, only Backup750 pool.
#	Add elapsed time display.
#	2016/05/26 - K. Raquel Sanborn - Added source dataset size printing.
#	2016/06/12 - K. Raquel Sanborn - Added Pool and Dataset attribute saving.
#	2016/07/19 - K. Raquel Sanborn - Fixed order for log file.
#	2016/08/27 - K. Raquel Sanborn - Add scrub of backup media before starting
#	the backup. Then check status, if any errors, abort backup.
#	2016/10/04 - K. Raquel Sanborn - Update to detect backup mount point. Put
#	copy of log file onto backup disk.
#	2016/10/07 - K. Raquel Sanborn - Simplify the backup directory structure.
#	2016/10/09 - K. Raquel Sanborn - For the larger disk, perform ZFS snapshot
#	after backup with date. Add command line parameter so that scrubs can be
#	skipped. For larger disk, added --delete option for Rsync.
#	2016/11/02 - K. Raquel Sanborn - Fixed backup ZFS and path specification.
#	2016/12/06 - K. Raquel Sanborn - Fixed source path. Also fixed ZFS source
#	dataset printing.
#	2016/12/07 - K. Raquel Sanborn - Fixed typo in log file output.
#	2016/12/31 - K. Raquel Sanborn - Add exclude entry for Media_archive.
#	2017/01/27 - K. Raquel Sanborn - Add "zpool history" output to backup.
#	2017/01/31 - K. Raquel Sanborn - Cleaned up log file a bit.
#	2017/04/29 - K. Raquel Sanborn - Test and updated documentation to allow
#	running in back ground.
#	2017/06/10 - K. Raquel Sanborn - Updated documentation to allow running
#	as batch job.
#	2017/07/18 - K. Raquel Sanborn - Added bail-out if initial pool status of
#	backup disk has errors.
#	2017/09/01 - K. Raquel Sanborn - Changed the Rsync parameters to remove the
#	"A" as that seems to prevent file deletion.
#
#   To be added:
#	2016/12/06 - K. Raquel Sanborn - Check source pool and dataset for
#	existance before proceeding. Then check destination pool and dataset
#	for existance before proceeding.
#	2017/03/31 - K. Raquel Sanborn - Allow backing up multiple source pools.
#	Have the script loop on pool name, instead of hostname. Plus, check for
#	the existance of the destination dataset(s) before starting the loop.
#	2016/11/13 - K. Raquel Sanborn - Base exclude list on Pool name. Thus,
#	multiple backup disks can be used. 8TB for all, 750GB all except media,
#	and 320GB for most, except media & ISOs.
#
#
##############################################################################
#
# User setable default parameters
#
export MY_LOGDIR=/var/log/local
export MY_SOURCE=/mnt/main
#
# Command line and run time parameters
#
MY_SCRIPT=`basename ${0}`
MY_SYSTEM=`uname -n | cut -f1 -d'.'`
CUR_DATE=`date +%Y\%m\%d`
export MY_SCRIPT MY_SYSTEM CUR_DATE
########################################
#
# Make the time parameter
#
########################################
print_elapsed_time () {
    MY_ELAPSED=$(( `date +%s`- ${MY_BEGIN_SECONDS} ))
    MY_HOURS=$(( ${MY_ELAPSED} / 3600 ))
    MY_MINS=$(( ${MY_ELAPSED} - ( ${MY_HOURS} * 3600 ) ))
    MY_MINS=$(( ${MY_MINS} / 60 ))
    MY_SECS=$(( ${MY_ELAPSED} - ( ${MY_MINS} * 60 ) - ( ${MY_HOURS} * 3600 ) ))
    if [ ${MY_HOURS} -eq 0 ]; then
        printf "(as .M:SS) = %d:%02d\n" ${MY_MINS} ${MY_SECS}
    else
        printf "(as .H:MM:SS) = %d:%02d:%02d\n" ${MY_HOURS} ${MY_MINS} ${MY_SECS}
    fi
}
########################################
#
# Create log file, (and directory tree if it does not already exist).
#
########################################
ls ${MY_LOGDIR} >/dev/null 2>/dev/null
if [ "$?" != "0" ]; then
    mkdir -m 775 -p ${MY_LOGDIR}
    if [ "$?" != "0" ]; then
        echo "${MY_SCRIPT}: Can't create log directory ${MY_LOGDIR}," \
      "exiting gracefully!"
        exit 1
    fi
    chgrp sys ${MY_LOGDIR}
fi
MY_LOGFILE=${MY_LOGDIR}/${MY_SYSTEM}_freenas_${$}.${CUR_DATE}
touch ${MY_LOGFILE}
if [ "$?" != "0" ]; then
    echo "${MY_SCRIPT}: Can't create logfile ${MY_LOGFILE}, exiting gracefully!"
    exit 2
fi
chmod 644 ${MY_LOGFILE}
chgrp sys ${MY_LOGFILE}
export MY_BEGIN_SECONDS=`date +%s`
#
# Print various parameters
#
echo "Command line  = ${0} ${*}" >>${MY_LOGFILE}
echo "Working dir   = `pwd`" >>${MY_LOGFILE}
echo "Host name     = ${MY_SYSTEM}" >>${MY_LOGFILE}
echo "Log file name = ${MY_LOGFILE}" >>${MY_LOGFILE}
#
# Detect source, currently derived from ${MY_SOURCE}"
#
MY_SOURCE_ZPOOL=`echo ${MY_SOURCE} | cut -f3 -d'/'`
echo "Source pool   = ${MY_SOURCE_ZPOOL}" >>${MY_LOGFILE}
echo "Source path   = ${MY_SOURCE}" >>${MY_LOGFILE}
#
# Detect destination, currently must start with Backup
#
MY_BACKUP_ZPOOL=`zpool list | grep "^Backup" | awk '{print $1}'`
echo "Backup pool   = ${MY_BACKUP_ZPOOL}" >>${MY_LOGFILE}
#
# Get ZFS name
#
MY_BACKUP_ZFS=`zfs list -r ${MY_BACKUP_ZPOOL} | grep ${MY_SYSTEM} | head -1 \
  | awk '{print $1}'`
echo "Backup ZFS    = ${MY_BACKUP_ZFS}" >>${MY_LOGFILE}
#
# Get backup path
MY_BACKUP_PATH=`zfs list ${MY_BACKUP_ZFS} | tail -1 | awk '{print $5}'`
echo "Backup path   = ${MY_BACKUP_PATH}" >>${MY_LOGFILE}
#
# Write some information about backup pool
#
echo "" >>${MY_LOGFILE}
echo "*************************************************************************" >>${MY_LOGFILE}
echo "************************ Source Pool and dataset ************************" >>${MY_LOGFILE}
echo " --- zpool list ${MY_SOURCE_ZPOOL}" >>${MY_LOGFILE}
zpool list ${MY_SOURCE_ZPOOL} >>${MY_LOGFILE}
echo "" >>${MY_LOGFILE}
echo " --- zfs list ${MY_SOURCE_ZPOOL}" >>${MY_LOGFILE}
zfs list ${MY_SOURCE_ZPOOL} >>${MY_LOGFILE}
echo "" >>${MY_LOGFILE}
echo " --- zpool status ${MY_SOURCE_ZPOOL}" >>${MY_LOGFILE}
zpool status ${MY_SOURCE_ZPOOL} >>${MY_LOGFILE}
echo "*************************************************************************" >>${MY_LOGFILE}
echo "************************ Backup Pool and dataset ************************" >>${MY_LOGFILE}
echo " --- zpool list ${MY_BACKUP_ZPOOL}" >>${MY_LOGFILE}
zpool list ${MY_BACKUP_ZPOOL} >>${MY_LOGFILE}
echo "" >>${MY_LOGFILE}
echo " --- zfs list ${MY_BACKUP_ZFS}" >>${MY_LOGFILE}
zfs list ${MY_BACKUP_ZFS} >>${MY_LOGFILE}
echo "" >>${MY_LOGFILE}
echo " --- zpool status ${MY_BACKUP_ZPOOL}" >>${MY_LOGFILE}
zpool status ${MY_BACKUP_ZPOOL} >>${MY_LOGFILE}
zpool status ${MY_BACKUP_ZPOOL} 2>/dev/null | grep 'errors: No known data errors' >/dev/null 2>&1
if [ ${?} != 0 ]; then
    echo "${MY_SCRIPT}: Before scrub, backup pool ${MY_BACKUP_ZPOOL} not clean!" >>${MY_LOGFILE}
    echo "Exiting gracefully!" >>${MY_LOGFILE}
    exit 3
fi
echo "*************************************************************************" >>${MY_LOGFILE}
echo "*************************** Scrub backup Pool ***************************" >>${MY_LOGFILE}
if [ "${MY_BACKUP_SCRUB}X" = "offX" ]; then
    echo "User requested no Scrub, skipping!" >>${MY_LOGFILE}
else
    echo "ZFS Pool scrub for ${MY_BACKUP_ZPOOL} beginning at "`date +%c`"." >>${MY_LOGFILE}
    echo " --- zpool scrub ${MY_BACKUP_ZPOOL}" >>${MY_LOGFILE}
    zpool scrub ${MY_BACKUP_ZPOOL} >>${MY_LOGFILE}
    echo "" >>${MY_LOGFILE}
#
# Loop
#
    echo "Looping on Pool status" >>${MY_LOGFILE}
    export MY_SCAN=1
    while [ ${MY_SCAN} -eq 1 ]; do
        sleep 20 
        zpool status ${MY_BACKUP_ZPOOL} 2>/dev/null | grep 'scan: scrub in progress' >/dev/null 2>&1
        if [ ${?} != 0 ]; then
            MY_SCAN=0
        fi
    done
    echo "" >>${MY_LOGFILE}
#
# End status
#
    echo " --- zpool status ${MY_BACKUP_ZPOOL}" >>${MY_LOGFILE}
    zpool status ${MY_BACKUP_ZPOOL} >>${MY_LOGFILE}
    zpool status ${MY_BACKUP_ZPOOL} 2>/dev/null | grep 'scan: scrub repaired 0' >/dev/null 2>&1
    if [ ${?} != 0 ]; then
        echo "${MY_SCRIPT}: After scrub, backup pool ${MY_BACKUP_ZPOOL} not clean!" >>${MY_LOGFILE}
        echo "Exiting gracefully!" >>${MY_LOGFILE}
        exit 4
    fi
fi
echo "*************************************************************************" >>${MY_LOGFILE}
echo "************************** Perform the backup ***************************" >>${MY_LOGFILE}
#
# OK, parameters checked, lets start the backups
#
echo "" >>${MY_LOGFILE}
echo "Backups for ${MY_SYSTEM} beginning at "`date +%c`"." >>${MY_LOGFILE}
echo "" >>${MY_LOGFILE}
#
# Only do full to 8TB disk
#
if [ "${MY_BACKUP_ZPOOL}X" = "Backup750X" ]; then
    echo "  rsync -aHSX --delete --stats \ " >>${MY_LOGFILE}
    echo "    --exclude='afp_test' --exclude='BUs' --exclude='oc-20170607-clone'  --exclude='plex_temp' --exclude='temp'  --exclude='test' \ " >>${MY_LOGFILE}
    echo "    ${MY_SOURCE}/ \ " >>${MY_LOGFILE}
    echo "    ${MY_BACKUP_PATH}/" >>${MY_LOGFILE}
    rsync -aHSX --delete --stats \
      --exclude='afp_test' --exclude='BUs' --exclude='oc-20170607-clone'  --exclude='plex_temp' --exclude='temp'  --exclude='test' \
      ${MY_SOURCE}/ \
      ${MY_BACKUP_PATH}/ 2>&1 \
      | awk '{print "  "$0}' >>${MY_LOGFILE}
else
    echo "  rsync -aHSX --delete --stats \ " >>${MY_LOGFILE}
    echo "    ${MY_SOURCE}/ \ " >>${MY_LOGFILE}
    echo "    ${MY_BACKUP_PATH}/" >>${MY_LOGFILE}
    rsync -aHSX --delete --stats \
      ${MY_SOURCE}/ \
      ${MY_BACKUP_PATH}/ 2>&1 \
      | awk '{print "  "$0}' >>${MY_LOGFILE}
    echo "" >>${MY_LOGFILE}
    echo "" >>${MY_LOGFILE}
    echo "  Snapshoting ZFS dataset to ${MY_BACKUP_ZFS}@${CUR_DATE}" >>${MY_LOGFILE}
    zfs snapshot ${MY_BACKUP_ZFS}@${CUR_DATE}
fi
echo "" >>${MY_LOGFILE}
echo "" >>${MY_LOGFILE}
echo "*************************************************************************" >>${MY_LOGFILE}
echo "************************ Pool & Dataset attr saving *********************" >>${MY_LOGFILE}
#
# Tell user what we are saving, and where.
#
echo "\
  zpool status    >${MY_BACKUP_PATH}/zpool_status.out
  zpool list      >${MY_BACKUP_PATH}/zpool_list.out
  zpool get all   >${MY_BACKUP_PATH}/zpool_get_all.out
  zpool history   >${MY_BACKUP_PATH}/zpool_history.out
  zfs list -t all >${MY_BACKUP_PATH}/zfs_list_t_all.out
  zfs get all     >${MY_BACKUP_PATH}/zfs_get_all.out" >>${MY_LOGFILE}
#
# Save copies of Pool and Dataset attributes
#
zpool status    >${MY_BACKUP_PATH}/zpool_status.out
zpool list      >${MY_BACKUP_PATH}/zpool_list.out
zpool get all   >${MY_BACKUP_PATH}/zpool_get_all.out
zpool history   >${MY_BACKUP_PATH}/zpool_history.out
zfs list -t all >${MY_BACKUP_PATH}/zfs_list_t_all.out
zfs get all     >${MY_BACKUP_PATH}/zfs_get_all.out
echo "*************************************************************************" >>${MY_LOGFILE}
echo "************************ Backup Pool and dataset ************************" >>${MY_LOGFILE}
echo " --- zpool list ${MY_BACKUP_ZPOOL}" >>${MY_LOGFILE}
zpool list ${MY_BACKUP_ZPOOL} >>${MY_LOGFILE}
echo "" >>${MY_LOGFILE}
echo " --- zfs list ${MY_BACKUP_ZFS}" >>${MY_LOGFILE}
zfs list ${MY_BACKUP_ZFS} >>${MY_LOGFILE}
echo "" >>${MY_LOGFILE}
echo " --- zpool status ${MY_BACKUP_ZPOOL}" >>${MY_LOGFILE}
zpool status ${MY_BACKUP_ZPOOL} >>${MY_LOGFILE}
echo "*************************************************************************" >>${MY_LOGFILE}
echo "************************ Backup time statistics *************************" >>${MY_LOGFILE}
#
# Close up log file
#
echo "" >>${MY_LOGFILE}
printf "Elapsed job time " >>${MY_LOGFILE}
print_elapsed_time >>${MY_LOGFILE}
echo "Backup completed for ${MY_SYSTEM} at "`date +%c`"." >>${MY_LOGFILE}
echo "" >>${MY_LOGFILE}
echo "*************************************************************************" >>${MY_LOGFILE}
chmod 444 ${MY_LOGFILE}
cp -p ${MY_LOGFILE} ${MY_BACKUP_PATH}/`basename ${MY_LOGFILE}`
#
# Exit gracefully
#
exit 0
