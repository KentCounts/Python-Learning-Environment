import os
import shutil
import argparse
import file_organizer

def main():
    print("Running main...")

    test_path = os.path.dirname(os.path.abspath(__file__))
    print("Path:", test_path)

    files = file_organizer.get_files_in_directory(test_path)

    for f in files:
        print(f)


if __name__ == "__main__":
    main()