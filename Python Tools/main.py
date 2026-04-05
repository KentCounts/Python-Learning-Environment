import os
import shutil
import argparse
import file_organizer

def main():
    print("Select a tool:")
    print("1. File Organizer")

    choice = input("Enter choice: ")

    if choice == "1":
        file_organizer.main()
    elif choice == "2":
        return


if __name__ == "__main__":
    main()