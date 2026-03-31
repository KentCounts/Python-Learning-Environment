# IMPORTS
# import os for file/directory operations
# import shutil for moving files
# import argparse (optional) for CLI arguments

# CONFIG
# define mapping of file extensions to folder names
#   ".pdf" > "Documents"
#   ".png" > "Images"

# define default target directory (optional)


# HELPER FUNCTIONS
# function: get_files_in_directory(path)
#   return list of files (exclude folders)

# function: get_file_extension(filename)
#   extract and return extension (lowercase)

# function: get_destination_folder(extension)
#   return folder name based on mapping
#   if extension not found → return "Other"

# function: create_folder_if_not_exists(base_path, folder_name)
#   check if folder exists
#   if not → create it


# CORE FUNCTIONALITY
# function: move_file(file_path, destination_folder)
#   construct destination path
#   move file using shutil

# function: organize_directory(target_path)
#   get all files in directory
#   loop through each file:
#       get extension
#       determine destination folder
#       ensure folder exists
#       move file


# ENTRY POINT
# function: parse_arguments()
#   define command line arguments
#   example:
#       path to organize

# main():
#   parse arguments
#   validate path
#   call organize_directory


# FUTURE IMPROVEMENT IDEAS
# handle duplicate filenames
# add dry-run mode (no actual moves)
# allow custom extension mappings via config file
# recursive directory support
# logging of moved files