-- This applescript will set the geographic EXIF data for all
--   selected images in iPhoto. A series of dialog boxes will pop 
--   up, asking you for the geographic information.
--  
--   You must have exiftool installed (google it).
--
-- Author: Andrew Turner (http://highearthorbit.com)
-- 
property exifToolOriginal : "_original"

-- MAKE SURE SUPPORT FOR ASSISTIVE DEVICES IS ACTIVE
tell application "System Events"
	if UI elements enabled is false then
		tell application "System Preferences"
			activate
			set current pane to pane id "com.apple.preference.universalaccess"
			display dialog "This script requires access for assistive evices be enabled." & return & return & "To continue, click the OK button and enter an administrative password in the forthcoming security dialog." with icon 1
		end tell
		set UI elements enabled to true
		if UI elements enabled is false then return "user cancelled"
		delay 1
	end if
end tell

tell application "iPhoto"
	activate
	try
		copy (my selected_images()) to these_images
		if these_images is false or (the count of these_images) is 0 then �
			error "Please select a single image."
		
		set locationName to "Home"
		set city to "Greely"
		set state to "ON"
		set countryName to "Canada"
		set countryCode to "CA"
		set |latitude| to "45,15,10.16"
		set northSouth to "N"
		set |longitude| to "75,34,55.64"
		set eastWest to "W"
		
		repeat with i from 1 to the count of these_images
			set this_photo to item i of these_images
			tell this_photo
				set the image_file to the image path
			end tell
			set exifCommand to "/sw/bin/exiftool " & " -iptc:Sub-location='" & locationName �
				& "' -xmp:City='" & city & "' -xmp:State='" & state & "' -xmp:Country='" & countryName �
				& "' -GPSMapDatum='WGS-84'" & " -gps:GPSLatitude='" & |latitude| & "' -gps:GPSLatitudeRef='" & northSouth �
				& "' -gps:GPSLongitude='" & |longitude| & "' -gps:GPSLongitudeRef='" & eastWest �
				& "' -xmp:GPSLatitude='" & |latitude| & northSouth & "' -xmp:GPSLongitude='" & |longitude| & eastWest & "' -xmp:GPSMapDatum='WGS-84'" & " -xmp:GPSVersionID='2.2.0.0' -iptc:City='" & city & "' -iptc:Province-State='" & state & "' -iptc:Country-PrimaryLocationCode='" & countryCode & "' -iptc:Country-PrimaryLocationName='" & countryName & �
				"'" & " '" & image_file & "'"
			set output to do shell script exifCommand
			
			
			--display dialog of output
			do shell script "rm '" & image_file & "'" & exifToolOriginal
		end repeat
		
tell application "System Events"
	tell process "iPhoto"
		tell menu bar 1
			tell menu bar item "Photos"
				tell menu "Photos"
					click menu item "Rescan for Location"
				end tell
			end tell
		end tell
	end tell
end tell
		
		display dialog "Done"
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
