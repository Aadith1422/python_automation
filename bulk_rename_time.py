import os 
from datetime import datetime
import time

# Define the folder containing the files to rename
folder_path = r"C:\Users\Aadith\Desktop\Python automation\for bulk rename with timestamp"
files = os.listdir(folder_path)  # Get a list of all files in the folder

# Rename Each File
for filename in files:
    # Extract the file extension (e.g., .txt, .jpg)
    file_ext = os.path.splitext(filename)[1]

    # Get current time with microsecond precision
    now = datetime.now()

    # Create a timestamp string in the format HHMMSSffffff (HourMinuteSecondMicrosecond)
    time_str = now.strftime("%H%M%S%f")

    # Build the new filename using timestamp + original extension
    new_name = f"{time_str}{file_ext}"

    # Build full paths for the source and destination files
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)

    # Rename the file
    os.rename(src, dst)

    # Print confirmation
    print(f"[+] Renamed: {filename} -> {new_name}")

    # Add a short delay to ensure unique timestamps
    time.sleep(0.001)

print("Rename complete")
