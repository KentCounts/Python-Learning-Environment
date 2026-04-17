# IMPORTS
# os for system interaction
# platform for OS/system details
# argparse for CLI
# optional:
#   psutil for advanced system metrics (CPU, memory, disk)

# default output mode (print to console)
# optional log file name
# optional refresh interval (for future live monitoring)

# function: get_os_info()
#   return operating system name and version
#   example:
#       Windows 10, Linux, etc.


# function: get_cpu_info()
#   return CPU details:
#       number of cores
#       processor name
#       usage percentage (if psutil used)


# function: get_memory_info()
#   return memory usage:
#       total RAM
#       used RAM
#       available RAM


# function: get_disk_info()
#   return disk usage:
#       total space
#       used space
#       free space


# function: get_environment_info()
#   return basic environment data:
#       current working directory
#       username (optional)

# function: format_size(bytes)
#   convert bytes → KB/MB/GB for readability


# function: display_system_info(info_dict)
#   format and print all collected info in readable way

# function: log_info(info_dict)
#   write system info to log file

# function: collect_system_info()
#   call all helper functions
#   store results in dictionary
#   return dictionary

# function: run()
#   collect system info
#   display results
#   optionally log results

# function: parse_arguments()
#   optional flags:
#       --log (write to file)
#       --verbose (extra details)

# function: run_interactive()
#   menu-driven:
#       show system info
#       optionally log

# function: main()
#   parse arguments
#   call run()

# if __name__ == "__main__":
#   main()


# FUTURE IMPROVEMENTS
# live monitoring mode (refresh loop)
# network info (IP, interfaces)
# process listing
# export to JSON
# cross-platform normalization improvements