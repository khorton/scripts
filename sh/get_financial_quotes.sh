#! /bin/sh
# Get latest mutual fund quotes, and look for buy and sell triggers
# source /sw/bin/init.sh
# /Users/kwh/sw_projects/hg/perl/get_canada_mut_fund_data.pl 1>> /Users/kwh/Documents/Misc/Financial_etc/mutual_funds/log.txt 2>&1
# /Users/kwh/Documents/Misc/Financial_etc/mutual_funds/mutual_buy_sell.py -s -b /Users/kwh/Documents/Misc/Financial_etc/mutual_funds/TD*.txt >>/Users/kwh/Documents/Misc/Financial_etc/mutual_funds/log.txt 2>&1
echo "=================================================" >> /Users/kwh/Library/Logs/GnuCash_Quotes.log
date | tee -a /Users/kwh/Library/Logs/GnuCash_Quotes.log
/Applications/GnuCash/Gnucash.app/Contents/MacOS/Gnucash --add-price-quotes=/Users/kwh/Dropbox/GnuCash/Horton\ Finances.gnucash | tee -a /Users/kwh/Library/Logs/GnuCash_Quotes.log

