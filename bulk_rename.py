import os
import random
import string

# Set the folder path where files are located
folder_path = r"C:\Users\Aadith\Desktop\Python automation"

# Set the length of the random string
length = 8

# Function to generate a random alphanumeric string
def random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

# Get list of all files in the folder
files = os.listdir(folder_path)

# used names to avoid duplicates
used_names = set()

for filename in files:
    file_ext = os.path.splitext(filename)[1]

    # Generate unique random filename
    while True:
        rand_str = random_string(length)
        new_name = f"{rand_str}{file_ext}"
        if new_name not in used_names:
            used_names.add(new_name)
            break

    # Full paths
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)

    # Rename the file
    os.rename(src, dst)
    print(f"{filename} -> {new_name}")

print("\n[+] Bulk random renaming completed successfully.")
