def draw_progress_bar(progress=0, total=100, fill_char="#", empty_char="-", bar_length=20):
   # Calculate the percentage completion
   percentage = (progress / total) * 100
   filled_length = int(bar_length * (progress / total))
   # Construct the progress bar string
   bar = fill_char * filled_length + empty_char * (bar_length - filled_length)
   # Format the progress text
   progress_text = f"({percentage:.0f}% complete)"
   # Combine bar and progress text
   progress_bar = f"{bar} {progress_text}"
   return progress_bar
# Sample Input 1
progress_bar = draw_progress_bar(progress=50)
print(progress_bar)
 
progress_bar = draw_progress_bar(progress=10)
print(progress_bar)
 
progress_bar = draw_progress_bar(progress=29)
print(progress_bar)