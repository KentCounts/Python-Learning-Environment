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

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Parse a log file for errors."
    )

    parser.add_argument(
        "file_path",
        nargs="?",
        default=DEFAULT_LOG_FILE,
        help="Path to log file (default: application.log)"
    )

    parser.add_argument(
        "--output",
        default=None,
        help="Optional output file to save parsed errors"
    )

    parser.add_argument(
        "--keywords",
        nargs="+",
        default=ERROR_KEYWORDS,
        help="Override default error keywords (e.g., ERROR WARNING CRITICAL)"
    )

    return parser.parse_args()


def run(file_path, output_file=None, keywords=None):
    if keywords is None:
        keywords = ERROR_KEYWORDS

    # validate file
    if not os.path.exists(file_path):
        print(f"Error: File does not exist: {file_path}")
        return

    if not os.path.isfile(file_path):
        print(f"Error: Path is not a file: {file_path}")
        return

    print(f"Parsing log file: {file_path}")

    errors = parse_log(file_path, keywords)

    display_errors(errors)

    if output_file:
        save_errors(errors, output_file)

    log_summary(len(errors))


def run_interactive():
    print("Log Parser Tool")

    file_path = input(f"Enter log file path (default: {DEFAULT_LOG_FILE}): ").strip()
    output_file = input("Enter output file (leave blank to skip): ").strip()

    if not file_path:
        file_path = DEFAULT_LOG_FILE

    if not output_file:
        output_file = None

    file_path = os.path.normpath(file_path)

    run(file_path, output_file)


def main():
    args = parse_arguments()
    run(args.file_path, args.output, args.keywords)

if __name__ == "__main__":
    main()

# FUTUR IMPROVEMENT IDEAS
# support JSON/CSV output
# regex-based custom parsing
# grouping errors by type
# count occurrences of each error
# time-range filtering
# live log monitoring (tail -f style)