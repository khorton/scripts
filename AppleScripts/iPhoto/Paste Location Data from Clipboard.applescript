tell application "iPhoto"
	activate
	try
		set clip_in to the clipboard
		--display dialog clip_in as text
		
		-- Split clipboard into items with : delimiter
		set AppleScript's text item delimiters to {":"}
		set clip_items to text items of clip_in
		set num_items to (count of clip_items)
		--display dialog "There are " & num_items & " items in the clipboard"
		if num_items < 3 then
			--display dialog "The clipboard does not have enough items" buttons {"OK"} with icon caution with title "ERROR"
			error "Cipboard has less than 3 items." number 9004
			
		else if num_items is greater than 3 then
			--display dialog "The clipboard has too many items" buttons {"OK"} with icon caution with title "ERROR"
			error "Cipboard has more than 3 items." number 9005
			--else
			--display dialog "Number of clipboard items OK"
		end if
		set AppleScript's text item delimiters to {""}
		
		-- Parse clipboard items
		set lat to item 1 of clip_items as real
		--display dialog "Latitude = " & lat
		set long to item 2 of clip_items as real
		--display dialog "Longitude = " & long
		set alt to item 3 of clip_items
		--display dialog "Altitude = " & alt
		
		-- confirm items in range
		if (lat < -90 or lat > 90) then
			error "Latitude out of range" number 9000
			--else
			--display dialog "Latitude in range:  " & lat
		end if
		
		if (long < -180 or long > 180) then
			error "Longitude out of range" number 9001
			--else
			--display dialog "Longitude in range: " & long
		end if
		
		try
			set dialogResult to display dialog "Paste the following data into photo?

Latitude: " & lat & "
Longitude: " & long with title "Confirm Paste" buttons {"Cancel", "Paste"} default button "Paste" with icon 1
			
		on error number -128
			-- user pressed "Cancel" button, so abort
			return
		end try
		
		copy (my selected_images()) to these_images
		if these_images is false or (the count of these_images) is 0 then
			--display dialog "Please select a single image." buttons "OK" with icon 0
			--display dialog the (count of these_images)
			error "Please select one or more images." number 9010
		else
			display dialog "Selection accepted"
			repeat with i from 1 to the count of these_images
				--set the keywordslist to ""
				set this_photo to item i of these_images
				tell this_photo
					set the latitude to lat
					set the longitude to long
					--set the altitude to alt
				end tell
			end repeat
			display dialog "Done"
			--set image_path to image path of item 1 of these_images -- works
			--set image_path to image path of these_images -- doesn't work
			--display dialog image_path
			--return image_path
		end if
	on error errStr number errorNumber
		-- If our own error number, warn about out of range data.
		if the errorNumber is equal to 9000 then
			display dialog "Latitude value out of range. Latitude must be between -90 and +90" buttons {"Close"} with icon 0
			return 0 -- Return the default value (0).
		else if the errorNumber is equal to 9001 then
			display dialog "Longitude value out of range. Longitude must be between -180 and +180" buttons {"Close"} with icon 0
			return 0 -- Return the default value (0).
		else if the errorNumber is equal to 9004 then
			display dialog "The clipboard had too few items! Try copying the location data again." buttons {"Close"} with icon 0
			return 0 -- Return the default value (0).
		else if the errorNumber is equal to 9005 then
			display dialog "The clipboard had too many items! Try copying the location data again." buttons {"Close"} with icon 0
			return 0 -- Return the default value (0).
		else if the errorNumber is equal to 9010 then
			display dialog "Please select one or more images." buttons {"Close"} with icon 0
			return 0 -- Return the default value (0).
		else
			display dialog "An unknown error occurred:  " & errorNumber as text
			-- An unknown error occurred. Resignal, so the caller
			-- can handle it, or AppleScript can display the number.
			error errStr number errorNumber
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