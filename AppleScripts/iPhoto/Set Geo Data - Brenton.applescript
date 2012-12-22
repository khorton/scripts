-- This applescript will set the geographic EXIF data for all
--   selected images in iPhoto. A series of dialog boxes will pop 
--   up, asking you for the geographic information.
--  
--   You must have exiftool installed (google it).
--
-- Author: Andrew Turner (http://highearthorbit.com)
-- 
property exifToolOriginal : "_original"

tell application "iPhoto"
	activate
	try
		copy (my selected_images()) to these_images
		if these_images is false or (the count of these_images) is 0 then Â
			error "Please select a single image."

		set locationName to "Brenton"
		set city to "Brenton"
		set state to "NS"
		set countryName to "Canada"
		set countryCode to "CA"
		set |latitude| to "43,57,45.04"
		set northSouth to "N"
		set |longitude| to "66,3,41.13"
		set eastWest to "W"
		
		repeat with i from 1 to the count of these_images
			set this_photo to item i of these_images
			tell this_photo
				set the image_file to the image path
			end tell
			set exifCommand to "/sw/bin/exiftool " & " -iptc:Sub-location='" & locationName Â
				& "' -xmp:City='" & city & "' -xmp:State='" & state & "' -xmp:Country='" & countryName Â
				& "' -GPSMapDatum='WGS-84'" & " -gps:GPSLatitude='" & |latitude| & "' -gps:GPSLatitudeRef='" & northSouth Â
				& "' -gps:GPSLongitude='" & |longitude| & "' -gps:GPSLongitudeRef='" & eastWest Â
				& "' -xmp:GPSLatitude='" & |latitude| & northSouth & "' -xmp:GPSLongitude='" & |longitude| & eastWest & "' -xmp:GPSMapDatum='WGS-84'" & " -xmp:GPSVersionID='2.2.0.0' -iptc:City='" & city & "' -iptc:Province-State='" & state & "' -iptc:Country-PrimaryLocationCode='" & countryCode & "' -iptc:Country-PrimaryLocationName='" & countryName & Â
				"'" & " '" & image_file & "'"
			set output to do shell script exifCommand
			--display dialog of output
			do shell script "rm '" & image_file & "'" & exifToolOriginal
		end repeat
		display dialog "Geo Exif write complete."
	on error error_message number error_number
		if the error_number is not -128 then
			display dialog error_message buttons {"Cancel"} default button 1
		end if
	end try
end tell


on selected_images()
	tell application "iPhoto"
		try
			-- get selection
			set these_items to the selection
			-- check for single album selected
			if the class of item 1 of these_items is album then error
			-- return the list of selected photos
			return these_items
		on error
			return false
		end try
	end tell
end selected_images