### Python - Exercise-4  

## Create A python program to practice Functions and Default Parameters Exercise: Customizable Progress Bar - This exercise involves creating a function called draw_progress_bar that generates a visual representation of progress as a text-based progress bar.

Function: draw_progress_bar(progress=0, total=100, fill_char="#", empty_char="-", bar_length=20)  

Parameters:  

progress (default: 0): An integer representing the current progress value (0 to total).  
total (default: 100): An integer representing the total value for the progress bar.  
fill_char (default: "#"): A string representing the character to be used for the filled portion of the bar.  
empty_char (default: "-"): A string representing the character to be used for the empty portion of the bar.  
bar_length (default: 20): An integer representing the total length of the progress bar.
Returns:  

A string containing the formatted progress bar text.  
Sample Input:  

Python  
# Draw a progress bar at 50% completion  
progress_bar = draw_progress_bar(progress=50)  
print(progress_bar)  

# Draw a custom progress bar with different characters and length  
custom_bar = draw_progress_bar(progress=75, total=200, fill_char="=", empty_char=" ", bar_length=30)  
print(custom_bar)  

Sample Output:  

██████████████████---- (50% complete)  
═══════════════════════>>>>> (75% complete)  

Challenge:  

Extend the function to display a dynamic progress bar that updates in real-time as the progress value   changes (suitable for use within a loop). You can utilize clear characters or animations for the filled portion.  
Allow the function to accept additional customization options (e.g., color codes for characters) using keyword arguments.  
