# IMPORTS
import os
import shutil
import argparse

# CONFIG
# define mapping of file extensions to folder names
EXTENSION_MAP = {
    # Documents
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",

    # Images
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".gif": "Images",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",

    # Video
    ".mp4": "Video",
    ".mov": "Video",

    # Archives
    ".zip": "Archives",
    ".rar": "Archives",

    # Code
    ".py": "Code",
    ".cpp": "Code",
    ".h": "Code",
}

DEFAULT_FOLDER = "Other"
DEFAULT_TARGET_DIRECTORY = os.getcwd()

# HELPER FUNCTIONS
# function: get_files_in_directory(path)
#   return list of files (exclude folders)
def get_files_in_directory(path):
    files = []

    # iterate through all entries in the directory
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)

        # check if entry is a file (not a directory)
        if os.path.isfile(full_path):
            files.append(full_path)

    return files

# function: get_file_extension(filename)
#   extract and return extension (lowercase)
def get_file_extension(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower()

# function: get_destination_folder(extension)
#   return folder name based on mapping
#   if extension not found → return "Other"
def get_destination_folder(extension):
    return EXTENSION_MAP.get(extension, DEFAULT_FOLDER)

# function: create_folder_if_not_exists(base_path, folder_name)
#   check if folder exists
#   if not → create it
def create_folder_if_not_exists(base_path, folder_name):
    folder_path = os.path.join(base_path, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path

# CORE FUNCTIONALITY
# function: move_file(file_path, destination_folder)
#   construct destination path
#   move file using shutil
def move_file(file_path, destination_folder):
    filename = os.path.basename(file_path)
    destination_path = os.path.join(destination_folder, filename)

    shutil.move(file_path, destination_path)

# function: organize_directory(target_path)
#   get all files in directory
#   loop through each file:
#       get extension
#       determine destination folder
#       ensure folder exists
#       move file
def organize_directory(target_path):
    files = get_files_in_directory(target_path)

    for file_path in files:
        filename = os.path.basename(file_path)

        # get extension
        extension = get_file_extension(filename)

        # find destination folder
        folder_name = get_destination_folder(extension)

        # check folder exists
        destination_folder = create_folder_if_not_exists(target_path, folder_name)

        # move file
        move_file(file_path, destination_folder)


# ENTRY POINT
# function: parse_arguments()
#   define command line arguments
#   example:
#       path to organize
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by type."
    )

    parser.add_argument(
        "path",
        nargs="?",  # optional argument
        default=DEFAULT_TARGET_DIRECTORY,
        help="Path to directory to organize (default: current directory)"
    )

    return parser.parse_args()

# run with manual input and not argparsing
def run(target_path):
    # validate path
    if not os.path.exists(target_path):
        print(f"Error: Path does not exist: {target_path}")
        return

    if not os.path.isdir(target_path):
        print(f"Error: Path is not a directory: {target_path}")
        return

    print(f"Organizing directory: {target_path}")

    organize_directory(target_path)

    print("Done.")

# menu choices and interactive mode. 
def run_interactive():
    print("File Organizer")

    path = input("Enter directory to organize (leave blank for current): ").strip()

    if not path:
        path = os.getcwd()

    path = os.path.normpath(path)

    run(path)

# main():
#   parse arguments
#   validate path
def main():
    args = parse_arguments()
    run(args.path)

if __name__ == "__main__":
    main()


# FUTURE IMPROVEMENT IDEAS
# handle duplicate filenames
# add dry-run mode (no actual moves)
# allow custom extension mappings via config file
# recursive directory support
# logging of moved files