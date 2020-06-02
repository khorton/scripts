#!/bin/bash

# Usage: sudo ./rsync-iMac.sh 03   

# logging notes at: https://stackoverflow.com/questions/4493525/rsync-what-means-the-f-on-rsync-logs
# and https://serverfault.com/questions/346356/how-to-add-timestamp-and-file-list-to-rsync-log

# to track time required for rsync to determine file list, in a separtate shell, run:
# while 1;do; sleep 60; if [ ps aux | grep rsync | wc -l -gt 2 ]; then; date | tee -a bu01.log; fi; done
# or 
# while 1;do; sleep 60; if [ ps aux | grep rsync | wc -l -gt 2 ]; then; date | tee -a bu02.log; fi; done

LOGDIR=~/logs/
LOG=$LOGDIR/$1.log
echo $LOG

echo "================================================" >> $LOG
echo "Start at" `date` >> $LOG
echo "—————————————————————————" >> $LOG

#rsync -aHSX -vvv --delete-before --progress --stats --itemize-changes --exclude-from '/root/rsync_exclude-list.txt' --out-format="%t %f %b" --delete-excluded /mnt/iocage/ /mnt/$1/iocage/ | tee -a $LOG
rsync -aHSx -v --delete-before --progress --stats --itemize-changes --exclude-from '/Users/kwh/sw_projects/git/scripts/Rsync/rsync_exclude-list.txt' --out-format="%t %f %b" --delete-excluded /Users/kwh/ /Volumes/iMac_$1/ | tee -a $LOG

echo "—————————————————————————" >> $LOG
echo "End at" `date` >> $LOG
echo "================================================" >> $LOG