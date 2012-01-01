#! /bin/bash

# read EXIF UserComment in each jpg and write it to ITPC Caption
#
# Usage: exif_comments2iptc *.jpg
# or: exif_comments2iptc file_name1.jpg file_name2.jpg ...
#
# exiv2 must be present on the machine where the script is run
# http://www.exiv2.org/
# http://pdb.finkproject.org/pdb/package.php/exiv2
# http://trac.macports.org/browser/trunk/dports/graphics/exiv2/Portfile
#
# script by Kevin Horton - released into the public domain

if [[ $# -lt 1 ]]; then
  echo "Usage: exif_comments2iptc one or more jpg file names ..."
  exit 1
fi

# pattern="Comment*[:space:]: (.+)"

for file_name
  do
    comment=`/sw/bin/exiftool -s3 -comment $file_name`
    if [[ $comment ]]; then
      echo "File: $file_name has comment: $comment"
      `/sw/bin/exiv2 -k -M "add Iptc.Application2.Caption $comment" $file_name`
      # `/sw/bin/exiftool −xmp:description="$comment" $file_name`
     else
       echo "No comment in $file_name"
     fi
  done