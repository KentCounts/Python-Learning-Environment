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


# function: is_error_line(line, keywords)
#   check if line contains any error keyword
#   return True/False


# function: extract_error_info(line)
#   parse useful parts of the log line
#   example:
#       timestamp
#       log level (ERROR, WARNING)
#       message
#   return structured data (dict or tuple)


# function: format_error_output(error_data)
#   convert structured data into readable string

# function: parse_log(file_path, keywords)
#   read all lines
#   loop through lines:
#       if is_error_line:
#           extract info
#           store results
#   return list of errors


# function: display_errors(errors)
#   print errors to console in readable format


# function: save_errors(errors, output_file)
#   write parsed errors to file

# function: log_summary(count)
#   log number of errors found


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