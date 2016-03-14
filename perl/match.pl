#!/usr/bin/perl 

use Getopt::Std;
use File::Slurp;
use File::Copy;
use File::Path;
use Cwd;
use strict;
use warnings;

my $dir = getcwd;
my $plate = shift;
# print $plate;

(my $ID, my $plate_name) = pick_plate_type($plate);

# replace "/" with "-" in plate names, as "/" is interpreted as a path separator
$plate_name =~ s/\//-/;

$plate =~ s/txt/pdf/;

mkpath(['Plates'], 1, 0777);

if (-e "$dir/Plates/$ID"){print "Dir exists\n"}
else {mkpath(["$dir/Plates/$ID"], 1, 0777)}

copy("$dir/$plate", "$dir/Plates/$ID/$plate_name");
# move("$dir/pg_0012.pdf", "$dir/pg_0012A.pdf");

sub pick_plate_type {
    my $Airport_ID ="";
    my $plate_title = "";
    
    my $CAP = shift(@_);
    # open(CAP_FILE, "<&=", $CAP);
    my $lines = read_file($CAP);

    # pages 0001 & 0002 are Intro pages, without page numbers printed on the page
    my $page_num = substr($CAP, -8, -4);
    return ("ZZZZ", "ZZZZ") if ($page_num == "0001" || $page_num == "0002");
    
    # Look for Roman numeral page numbers, on the Intro pages
    return ("ZZZZ", "ZZZZ") if $lines =~ /^i[xv]|v?i{0,3} Canada Air Pilot/;
    
    # Return Aerodrome Charts
    if ($lines =~ /(\w{4})-AD/){
        $Airport_ID = $1;
        return ($Airport_ID, "Aerodrome Chart.pdf");
    }

    # Return Heliport Charts
    if ($lines =~ /(\w{4})-HP/){
        $Airport_ID = $1;
        return ($Airport_ID, "Heliport Chart.pdf");
    }
    
    # Return Visual Approach Charts
    if ($lines =~ /(\w{4})-VAP/){
        $Airport_ID = $1;
        return ($Airport_ID, "Visual Approach Chart.pdf");
    }
    
    # Return Instrument Approach Charts
    # problem children: 0086
    if ($lines =~ /(\w{4})-IAP/){
        $Airport_ID = $1;
        # if ($lines =~ /(.{3,}? RWY .{3,})/){
        if ($lines =~ /^(.{3,}? RWY .{2,})$/m){
            $plate_title = $1;
        }
        # elsif ($lines =~ /^(.*?RNAV|VOR|NDB.*?)$/m){
        elsif ($lines =~ /^((VOR|NDB|RNAV).*?)$/m){
            $plate_title = $1;
        }
        return ($Airport_ID, $plate_title . ".pdf");
    }    
    

    
    return ("????", "????");
    
}
