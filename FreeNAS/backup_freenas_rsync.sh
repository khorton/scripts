#!/bin/bash

# Backup FreeNAS BigBertha server

rsync -aHSX --delete --progress --stats --exclude-from '/root/rsync_exclude-list.txt' /mnt/main/ /mnt/bu01/ | tee -a /root/bu.log
