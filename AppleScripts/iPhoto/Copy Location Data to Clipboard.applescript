tell application "iPhoto"
	activate
	try
		--display dialog "in script"
		copy (my selected_images()) to these_images
		if these_images is false or (the count of these_images) is not 1 then
			display dialog "Please select a single image."
			error "Please select a single image."
		else
			try
				set lat to latitude of item 1 of these_images
				set lat_text to lat as text
				set long to longitude of item 1 of these_images
				set long_text to long as text
				set alt to altitude of item 1 of these_images
				set alt_text to alt as text
				set AppleScript's text item delimiters to {":"}
				set the clipboard to {lat_text, long_text, alt_text} as text
				set AppleScript's text item delimiters to {""}
				
			on error errMsg number errorNumber
				display dialog "An unknown error occurred:  " & errorNumber as text
			end try
			set lat_text to lat as text --works
			return lat
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