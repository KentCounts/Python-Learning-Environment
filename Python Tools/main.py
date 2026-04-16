import os
import shutil
import argparse
import file_organizer
import batch_renamer

def main():
    while True:
        print("\nAutomation Tools")
        print("1. File Organizer")
        print("2. Batch Renamer")
        print("3. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            file_organizer.run_interactive()

        elif choice == "2":
            batch_renamer.run_interactive()

        elif choice == "3":
            print("Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()