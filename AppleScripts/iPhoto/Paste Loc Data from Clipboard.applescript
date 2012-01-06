tell application "iPhoto"
	activate
	try
		--display dialog "in script"
		set clip_in to the clipboard
		--display dialog clip_in as text
		set AppleScript's text item delimiters to {":"}
		set clip_items to text items of clip_in
		set num_items to (count of clip_items)
		display dialog "There are " & num_items & " items in the clipboard"
		if num_items = 0 then
			display dialog "The clipboard is empty" buttons {"OK"} with icon caution with title "ERROR"
		else if num_items is greater than 3 then
			display dialog "The clipboard has too many items" buttons {"OK"} with icon caution with title "ERROR"
		else
			display dialog "Number of clipboard items OK"
		end if
		set AppleScript's text item delimiters to {""}
		set lat to item 1 of clip_items as real
		display dialog "Latitude = " & lat
		set long to item 2 of clip_items
		display dialog "Longitude = " & long
		set alt to item 3 of clip_items
		display dialog "Altitude = " & alt
		--if ((lat ² 90) and (lat ³ -90)) then
(*		if (lat > 90) then
			error "Latitude out of range - too high" number -12000
		else if (lat < -90) then
			error "Latitude out of range - too low" number -12001
		else
			display dialog "Latitude2 = " & lat
		end if*)
		if (lat < -90 or lat > 90) then 
		error "Latitude out of range" number 12000
		else
		display dialog "Latitude2 = " & lat
		end if
		display dialog "Finished clip_in"
		copy (my selected_images()) to these_images
		if these_images is false or (the count of these_images) is 0 then
			display dialog "Please select a single image."
			display dialog the (count of these_images)
			error "Please select one or more images."
		else
			display dialog "Selection accepted"
			repeat with i from 1 to the count of these_images
				set the keywordslist to ""
				set this_photo to item i of these_images
				tell this_photo
					set the image_file to the image path
					set the image_title to the title
					set the image_filename to the image filename
					set the image_comment to the comment
					set the assigned_keywords to the name of keywords
				end tell
			end repeat
			set lat_text to lat as text --works
			return lat
			--set image_path to image path of item 1 of these_images -- works
			--set image_path to image path of these_images -- doesn't work
			--display dialog image_path
			--return image_path
		end if
	on error errMsg number errorNumber
		--display dialog "Paste Location Failed" buttons {"OK"} with icon caution with title "ERROR"
		display dialog "An unknown error occurred:  " & errorNumber as text
		
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