# IMPORTS
import os
import shutil
import argparse

# CONFIG
# define mapping of file extensions to folder names
#   ".pdf" > "Documents"
#   ".png" > "Images"
# define default target directory (optional)

EXTENSION_MAP = {
    # ".pdf": "Documents",
    # ".png": "Images",
    # ".jpg": "Images",
    # ".mp3": "Audio",
}

# HELPER FUNCTIONS
# function: get_files_in_directory(path)
#   return list of files (exclude folders)
def get_files_in_directory(path):
    return []

# function: get_file_extension(filename)
#   extract and return extension (lowercase)
def get_file_extension(filename):
    return ""

# function: get_destination_folder(extension)
#   return folder name based on mapping
#   if extension not found → return "Other"
def get_destination_folder(extension):
    return ""

# function: create_folder_if_not_exists(base_path, folder_name)
#   check if folder exists
#   if not → create it
def create_folder_if_not_exists(base_path, folder_name):
    pass

# CORE FUNCTIONALITY
# function: move_file(file_path, destination_folder)
#   construct destination path
#   move file using shutil
def move_file(file_path, destination_folder):
    pass

# function: organize_directory(target_path)
#   get all files in directory
#   loop through each file:
#       get extension
#       determine destination folder
#       ensure folder exists
#       move file
def organize_directory(target_path):
    pass


# ENTRY POINT
# function: parse_arguments()
#   define command line arguments
#   example:
#       path to organize
def parse_arguments():
    return None

# main():
#   parse arguments
#   validate path
def main():
    pass

if __name__ == "__main__":
    main()


# FUTURE IMPROVEMENT IDEAS
# handle duplicate filenames
# add dry-run mode (no actual moves)
# allow custom extension mappings via config file
# recursive directory support
# logging of moved files