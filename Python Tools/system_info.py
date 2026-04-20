import os
import platform
import argparse
import psutil


def get_os_info():
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }

def get_cpu_info():
    return {
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True),
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
    }

def get_memory_info():
    mem = psutil.virtual_memory()

    return {
        "total": mem.total,
        "available": mem.available,
        "used": mem.used,
        "percent_used": mem.percent,
    }

def get_disk_info():
    disk = psutil.disk_usage('/')

    return {
        "total": disk.total,
        "used": disk.used,
        "free": disk.free,
        "percent_used": disk.percent,
    }

def get_environment_info():
    return {
        "current_working_directory": os.getcwd(),
        "user": os.getenv("USERNAME") or os.getenv("USER"),
        "home_directory": os.path.expanduser("~"),
    }

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