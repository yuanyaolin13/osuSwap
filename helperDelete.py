import os
import shutil

file_path = "skins/anime_copy"

# Check if the file exists before deleting
if os.path.exists(file_path):
    shutil.rmtree(file_path)
    print(f"Deleted file: {file_path}")
else:
    print(f"File not found: {file_path}")

osk_file = "skins/anime_copy.osk"

# Check if the file exists before deleting
if os.path.exists(osk_file):
    os.remove(osk_file)
    print(f"Deleted file: {osk_file}")
else:
    print(f"File not found: {osk_file}")