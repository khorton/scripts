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

use Cwd;
use File::Copy;
use File::Path;
use File::Remove 'remove';
use File::Slurp;
use File::Temp;
use Getopt::Std;
use strict;

getopt('o');
use vars qw/$opt_o/;
# my $tempdir = File::Temp->newdir();
# my $dir = getcwd;

my $dir = getcwd;

sub process_eCAP {
    my $CAP = shift(@_);

    # split file into single page pdfs
    # system("$pdftk '$dir/$CAP' burst");
    system("$pdftk '$CAP' burst");
    
    # create text version of each page
    my @plates = glob "pg*.pdf";

    foreach my $plate (@plates){
        system("pdftotext $plate");

        (my $plate_text = $plate) =~ s/pdf/txt/;
        (my $ID, my $plate_name) = pick_plate_type($plate_text);
        print "$plate, $ID, $plate_name\n";
        if (($ID eq "ZZZZ") || ($ID eq "????")){next}
        
        # replace "/" with "-", as "/" is used as path separator
        $plate_name =~ s/\//-/;
        
        mkpath(['Plates'], 0, 0777);
        # if (-e "$dir/Plates/$ID"){print "Dir exists\n"}
        # else {mkpath(["$dir/Plates/$ID"], 1, 0777)}
        unless (-e "$dir/Plates/$ID"){mkpath(["$dir/Plates/$ID"], 0, 0777)}
        move("$dir/$plate", "$dir/Plates/$ID/$plate_name");
        # remove($plate_text);
    }
}

# sub parse_plate {
#     my $plate = shift;
#
# }

sub pick_plate_type {
    
    my $Airport_ID ="";
    my $plate_title = "";
    my $AD_Name = "";
    
    my $CAP = shift(@_);
    # print "Plate is $CAP\n";
    # open(CAP_FILE, "<&=", $CAP);
    my $lines = read_file($CAP);

    # pages 0001 & 0002 are Intro pages, without page numbers printed on the page
    # my $page_num = substr($CAP, -8, -4);
    # return ("ZZZZ", "ZZZZ") if ($page_num == "0001" || $page_num == "0002");
    
    # Look for Roman numeral page numbers, on the Intro pages
    # return ("ZZZZ", "ZZZZ") if $lines =~ /^i[xv]|v?i{0,3} Canada Air Pilot/;
    
    # Return multi-page Aerodrome Charts
    if ($lines =~ /^(\w{4})-AD-(\d)/m){
        $Airport_ID = $1;
        my $AD_Chart_pg_num = $2;
        if ($lines =~ /^(.+?), (NL|NS|PE|NB|QC|ON|MB|SK|AB|BC|NU|NT|YK)/m){
            $AD_Name = $1;
        }
        if ($AD_Name =~ /\w{4}-AD (.+)?/){$AD_Name = $1}
        return ($Airport_ID, "$AD_Name Aerodrome Chart.pdf - page $AD_Chart_pg_num.pdf");
    }
    
    # Return single-page Aerodrome Charts
    if ($lines =~ /^(\w{4})-AD/m){
        $Airport_ID = $1;
        if ($lines =~ /^(.+?), (NL|NS|PE|NB|QC|ON|MB|SK|AB|BC|NU|NT|YK)/m){
            $AD_Name = $1;
        }
    if ($AD_Name =~ /\w{4}-AD (.+)?/){$AD_Name = $1}
    return ($Airport_ID, "$AD_Name Aerodrome Chart.pdf");
    }
    
    # Return Heliport Charts
    if ($lines =~ /^(\w{4})-HP/m){
        $Airport_ID = $1;
        if ($lines =~ /^(.+?), (NL|NS|PE|NB|QC|ON|MB|SK|AB|BC|NU|NT|YK)/m){
            $AD_Name = $1;
        }
        return ($Airport_ID, "$AD_Name Heliport Chart.pdf");
    }
    
    # Return Visual Approach Charts
    if ($lines =~ /^(\w{4})-VAP/m){
        $Airport_ID = $1;
        return ($Airport_ID, "Visual Approach Chart.pdf");
    }
    
    # Return Instrument Approach Charts
    if ($lines =~ /^(\w{4})-IAP/m){
        $Airport_ID = $1;
        # if ($lines =~ /(.{3,}? RWY .{3,})/){
        if ($lines =~ /^(.{3,}? RWY .{2,})$/m){
            $plate_title = $1;
        }
        # elsif ($lines =~ /^(.*?RNAV|VOR|NDB.*?)$/m){
        elsif ($lines =~ /^((COPTER|VOR|NDB|RNAV).*?)$/m){
            $plate_title = $1;
        }
        return ($Airport_ID, $plate_title . ".pdf");
    }    
    
    # Return multi-page STARs
    if ($lines =~ /^(\w{4})-STAR-\d+(\w)/m){
        $Airport_ID = $1;
        my $STAR_pg_num = $2;
        $STAR_pg_num = ord($STAR_pg_num) - 64;
        if ($lines =~ /^(\w{3,25}) \w{3,5} ARR \(\w{1,5}\.\w{5}(\d)\)/m){
            my $arr_name = $1;
            my $arr_num = $2;
            $plate_title = "STAR - $arr_name$arr_num - page $STAR_pg_num";
        }
        else {
            # print $Airport_ID, $STAR_pg_num;
            return ("AAAA", $CAP);
        }
        return ($Airport_ID, $plate_title . ".pdf");
    }
    
    # Return single-page STARs
    if ($lines =~ /^(\w{4})-STAR/m){
        $Airport_ID = $1;
        if ($lines =~ /^(\w{3,25}) \w{3,5} ARR \(\w{3,5}\.\w{5}(\d)\)/m){
            my $arr_name = $1;
            my $arr_num = $2;
            $plate_title = "STAR - $arr_name$arr_num";
        }
        else {
            # print $Airport_ID, "Single page STAR";
            return ("BBBB", $CAP);
        }
        return ($Airport_ID, $plate_title . ".pdf");
    }
    
    # Return multi-page SIDs
    if ($lines =~ /^(\w{4})-SID-\d+(\w)/m){
        $Airport_ID = $1;
        my $SID_pg_num = $2;
        $SID_pg_num = ord($SID_pg_num) - 64;
        if ($lines =~ /^(\w{1,25}) \w{3,5} DEP \(.+?(\d).*\)/m){
            my $dep_name = $1;
            my $dep_num = $2;
            $plate_title = "SID - $dep_name$dep_num - page $SID_pg_num";
        }
        else {
            print $Airport_ID, $SID_pg_num;
            return ("CCCC", $CAP);
        }
        return ($Airport_ID, $plate_title . ".pdf");
    }
    
    # Return single-page SIDs
    if ($lines =~ /^(\w{4})-SID/m){
        $Airport_ID = $1;
        if ($lines =~ /(\w{1,25}) \w{3,5} DEP \(\w{3,5}\.\w{5}(\d)\)/){
            my $dep_name = $1;
            my $dep_num = $2;
            $plate_title = "SID - $dep_name$dep_num";
        }
        else {
            return ("DDDD", $CAP);
        }
        return ($Airport_ID, $plate_title . ".pdf");
    }
    
    

    
    return ("ZZZZ", $CAP);
    
}

# print our @ARGV;

# print $dir;

foreach our $CAP (@ARGV){
    print "$CAP\n";
    process_eCAP ($CAP);
}
