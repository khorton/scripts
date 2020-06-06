#! /sw/bin/zsh

# script creates a folder structure for a new KHAS FY
# script will not clobber an already existing directory

# Steps: 
# 1. manually create the top level FY directory
# 2. run the script from inside the new FY directory

echo $PWD
mkdir "$PWD/BMO Bank Account"
mkdir "$PWD/BMO MasterCard"
mkdir "$PWD/CCA"
mkdir "$PWD/Capital"
mkdir "$PWD/Cell Phone"
mkdir "$PWD/Corporation"
mkdir "$PWD/Delivery and Express"
mkdir "$PWD/Equipment"
mkdir "$PWD/GST"
mkdir "$PWD/Income"
mkdir "$PWD/Maint and Repairs"
mkdir "$PWD/Management and Admin"
mkdir "$PWD/Meals and Entertainment"
mkdir "$PWD/Office Expenses"
mkdir "$PWD/Professional Fees"
mkdir "$PWD/SW Licenses"
mkdir "$PWD/Taxes"
mkdir "$PWD/Travel Receipts"