import os
import argparse
import re

# default log file
DEFAULT_LOG_FILE = "application.log"

# default output file
DEFAULT_OUTPUT_FILE = "parsed_errors.txt"

# keywords for errors
ERROR_KEYWORDS = ["ERROR", "WARNING", "CRITICAL"]

# case sensitivity
CASE_SENSITIVE = False

def read_log_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log file not found: {file_path}")

    if not os.path.isfile(file_path):
        raise ValueError(f"Path is not a file: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()


def is_error_line(line, keywords):
    if not CASE_SENSITIVE:
        line = line.lower()
        keywords = [k.lower() for k in keywords]

    return any(keyword in line for keyword in keywords)


def extract_error_info(line):
    line = line.strip()

    # regex for: timestamp + level + message
    pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w+)\s+(.*)$"
    match = re.match(pattern, line)

    if match:
        timestamp, level, message = match.groups()
        return {
            "timestamp": timestamp,
            "level": level,
            "message": message
        }

    # fallback if line doesn't match format
    return {
        "timestamp": "N/A",
        "level": "UNKNOWN",
        "message": line
    }


def format_error_output(error_data):
    return f"[{error_data['level']}] {error_data['timestamp']} - {error_data['message']}"

def parse_log(file_path, keywords):
    lines = read_log_file(file_path)
    errors = []

    for line in lines:
        if is_error_line(line, keywords):
            error_data = extract_error_info(line)
            errors.append(error_data)

    return errors


def display_errors(errors):
    if not errors:
        print("No errors found.")
        return

    print("\n=== Parsed Errors ===\n")

    for error in errors:
        print(format_error_output(error))


def save_errors(errors, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        for error in errors:
            file.write(format_error_output(error) + "\n")

    print(f"Errors saved to: {output_file}")


def log_summary(count):
    log_file = "log_parser_summary.txt"

    with open(log_file, "a") as file:
        file.write(f"Errors found: {count}\n")


# function: parse_arguments()
#   arguments:
#       log file path
#       optional output file
#       optional keyword override


# function: run(file_path, output_file=None)
#   validate file exists
#   call parse_log
#   display results
#   optionally save results


# function: run_interactive()
#   prompt user for:
#       log file path
#       output file (optional)
#   call run()


# function: main()
#   parse CLI arguments
#   call run()



# if __name__ == "__main__":
#   main()

# FUTUR IMPROVEMENT IDEAS
# support JSON/CSV output
# regex-based custom parsing
# grouping errors by type
# count occurrences of each error
# time-range filtering
# live log monitoring (tail -f style)