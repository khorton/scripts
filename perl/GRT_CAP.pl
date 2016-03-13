#!/usr/bin/perl -w

#
# 
# Convert Nav Canada eCAP PDF files to format suitable for GRT EFIS
#
# Usage: perl GRT_CAP.pl e-CAP4_4February2016.pdf
#    or: perl GRT_CAP.pl e-CAP*.pdf
#
# The default is to create a Plates.zip output in the same folder as the 
# original eCAP pdfs.  If desired, the output directory can be specified
# with the -o flag:
# 
# perl GRT_CAP.pl -o "/Users/kwh/Documents/GRT Plates" e-CAP4_4February2016.pdf

# Edit the following path:
# location of pdftotext
my $pdftotext = '/sw/bin/pdftotext';
my $pdftk     = '/sw/bin/pdftk';

use File::Temp;
use Getopt::Std;
use Cwd;
use strict;

getopt('o');
use vars qw/$opt_o/;
# my $tempdir = File::Temp->newdir();
# my $dir = getcwd;

sub process_eCAP {
    my $CAP = shift(@_);

    # split file into single page pdfs
    # system("$pdftk '$dir/$CAP' burst");
    system("$pdftk '$CAP' burst");
    
    # process each page
    my @pages = glob "pg*.pdf";

    foreach my $page (@pages){
        system("pdftotext $page")
    }
    
    
}

# print our @ARGV;

# print $dir;

foreach our $CAP (@ARGV){
    print "$CAP\n";
    process_eCAP ($CAP);
}
