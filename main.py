import glob
import os
import shutil

# THESE ARE TO BE USER CHANGED.
NON_ANIME = "skins/CHANGEME"
ANIME = "skins/CHANGEME"


PATTERNS = [
    "menu-back-*.png",
    "ranking-*.png",
    "mode-*.png",
    "section-*.png",
    "selection-mod-*.png",
    "selection-*.png",
    "play-skip-*.png",
]
NON_PATTERNS = [
    "pause-overlay.png",
    "menu-background.png",
    "menu-background.jpg",
    "fail-background.png",
    "fail-background.jpg",
    "background.png",
    "background.jpg",
]
AUDIO_FILES = [
    "combobreak.wav",
    "sectionfail.wav",
    "sectionpass.wav",
    "failsound.wav",
]

def start(source_folder):
    copy(source_folder);
    replace(NON_ANIME, f"{ANIME}_copy")
    output()

# Create copy of the "ANIME" folder
def copy(source_folder):

    parent_dir = os.path.dirname(source_folder)
    folder_name = os.path.basename(source_folder)
    new_folder_name = f"{folder_name}_copy"

    destination_folder = os.path.join(parent_dir, new_folder_name)

    shutil.copytree(source_folder, destination_folder)
    print(f"Copied '{source_folder}' to '{destination_folder}'")


# this will OVERWRITE files
def replace(source_folder, destination_folder):
    print(source_folder)
    print(destination_folder)
    if not os.path.exists(source_folder):
        raise FileNotFoundError(f"Source folder does not exist: {source_folder}")
    if not os.path.exists(destination_folder):
        raise FileNotFoundError(f"Destination folder does not exist: {destination_folder}")

    # Does unique files first
    for filename in NON_PATTERNS:
        animeFileToReplace = os.path.join(source_folder, filename)
        nonAnimeFile = os.path.join(destination_folder, filename)

        if os.path.isfile(animeFileToReplace) and os.path.isfile(nonAnimeFile):
            shutil.copy2(animeFileToReplace, nonAnimeFile)  # Overwrites destination
            print(f"Replaced '{filename}'")
        else:
            print(f"Skipped '{filename}' (missing in source or destination)")

    # Replace sounds next
    for audio in AUDIO_FILES:
        animeFileToDelete = os.path.join(destination_folder, audio)
        if os.path.exists(animeFileToDelete):
            print(animeFileToDelete)
            os.remove(animeFileToDelete)
            print(f"Deleted '{audio}'")
        else:
            print(f"Skipped '{audio}', does not exist?")

    # Next, moves on to the patterns, removes them first in destination, and then all of them are
    # replaced by the source folder
    # Remove files
    for pattern in PATTERNS:
        for file_path in glob.glob(os.path.join(destination_folder, pattern)):
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Removed: {file_path}")

    # Copies from the source
    for pattern in PATTERNS:
        # Find matching files in the source folder
        for src_path in glob.glob(os.path.join(source_folder, pattern)):
            if os.path.isfile(src_path):
                dest_path = os.path.join(destination_folder, os.path.basename(src_path))
                shutil.copy2(src_path, dest_path)
                print(f"Copied: {src_path} -> {dest_path}")

    print("DONE COPYING")

def output():
    shutil.make_archive(f"{ANIME}_copy", 'zip', f"{ANIME}_copy")
    os.rename(f"{ANIME}_copy.zip", f"{ANIME}_copy.osk")

# First copies, then replaces
start(ANIME)

