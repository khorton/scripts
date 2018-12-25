#!/bin/bash

# Backup FreeNAS BigBertha server

export MY_LOGDIR=/root

MY_SCRIPT=`basename ${0}`
MY_SYSTEM=`uname -n | cut -f1 -d'.'`
CUR_DATE=`date +%Y\%m\%d`
export MY_SCRIPT MY_SYSTEM CUR_DATE

zpool scrub bu01

rsync -aHSX --delete --progress --stats --exclude-from '/root/rsync_exclude-list.txt' /mnt/main/ /mnt/bu01/ | tee -a /root/bu01.log
