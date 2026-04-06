import os
import shutil
import argparse
import file_organizer

def main():
    print("Automation Tools")
    print("1. File Organizer")
    print("2. Exit")

    choice = input("Select an option: ").strip()

    if choice == "1":
        file_organizer.run_interactive()
    elif choice == "2":
        print("Exiting.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()