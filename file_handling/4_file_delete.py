import os.path

from constants import path_to_dir

path = os.path.join(path_to_dir, "file_handling", "first_file1.txt")

if os.path.exists(path):
    os.remove(path)
else:
    print("File already deleted!")