# IMPORTS
import os
import argparse

# CONFIG
DEFAULT_TARGET_DIRECTORY = os.getcwd()
DEFAULT_PATTERN = "file_{index}"
PRESERVE_EXTENSION = True
START_INDEX = 1
LOG_FILE = "renamer_log.txt"

# NOTE:
# pattern must include "{index}" or filenames will collide
# example valid patterns:
#   "file_{index}"
#   "image_{index}"
#   "renamed_{index}"

def get_files_in_directory(path):
    files = []

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)

        if os.path.isfile(full_path):
            files.append(full_path)

    return files


def generate_new_name(filename, index, pattern):
    name, ext = os.path.splitext(filename)

    # build name using pattern
    new_name = pattern.format(index=index)

    if PRESERVE_EXTENSION:
        new_name += ext

    return new_name

def resolve_name_conflict(directory, new_name):
    base_name, ext = os.path.splitext(new_name)
    candidate = new_name
    counter = 1

    # loop until find name that does not exist
    while os.path.exists(os.path.join(directory, candidate)):
        candidate = f"{base_name} ({counter}){ext}"
        counter += 1

    return candidate

def rename_file(old_path, directory, new_name):
    new_path = os.path.join(directory, new_name)

    # perform rename
    os.rename(old_path, new_path)

    # log + print
    log_message = f"Renamed: {os.path.basename(old_path)} → {new_name}"
    print(log_message)
    log_action(log_message)

def batch_rename(target_path, pattern):
    files = get_files_in_directory(target_path)

    index = START_INDEX

    for file_path in files:
        filename = os.path.basename(file_path)

        # generate new name
        new_name = generate_new_name(filename, index, pattern)

        # resolve conflicts
        safe_name = resolve_name_conflict(target_path, new_name)

        # rename file
        rename_file(file_path, target_path, safe_name)

        # increment index
        index += 1

def log_action(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(message + "\n")


# parse_arguments()
#   define command line arguments:
#       path (optional)
#       naming pattern (optional)


# run(target_path, pattern)
#   validate path
#   call batch_rename


# function: run_interactive()
#   prompt user for:
#       directory path
#       naming pattern
#   apply defaults if blank
#   call run()


# function: main()
#   parse arguments
#   call run()

# if __name__ == "__main__":
#   main()

# FUTURE IMPROVEMENT IDEAS=
# support prefix/suffix modes
# preserve original filename partially
# regex-based renaming
# recursive directory support
# dry-run mode
# undo functionality