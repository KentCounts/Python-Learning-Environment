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

def format_size(bytes_value):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if bytes_value < 1024:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024

    return f"{bytes_value:.2f} PB"

def log_info(info):
    with open(LOG_FILE, "a") as log_file:
        log_file.write("=== System Info Log ===\n")

        for section, data in info.items():
            log_file.write(f"\n[{section.upper()}]\n")

            for key, value in data.items():
                log_file.write(f"{key}: {value}\n")

        log_file.write("\n")

def collect_system_info():
    info = {
        "os": get_os_info(),
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "environment": get_environment_info(),
    }

    return info

def display_system_info(info):
    print("\n=== System Information ===\n")
    # OS
    print("Operating System:")
    for key, value in info["os"].items():
        print(f"  {key}: {value}")
    print()

    # CPU
    print("CPU:")
    for key, value in info["cpu"].items():
        print(f"  {key}: {value}")
    print()

    # Memory
    print("Memory:")
    mem = info["memory"]
    print(f"  total: {format_size(mem['total'])}")
    print(f"  used: {format_size(mem['used'])}")
    print(f"  available: {format_size(mem['available'])}")
    print(f"  percent_used: {mem['percent_used']}%")
    print()

    # Disk
    print("Disk:")
    disk = info["disk"]
    print(f"  total: {format_size(disk['total'])}")
    print(f"  used: {format_size(disk['used'])}")
    print(f"  free: {format_size(disk['free'])}")
    print(f"  percent_used: {disk['percent_used']}%")
    print()

    # Environment
    print("Environment:")
    for key, value in info["environment"].items():
        print(f"  {key}: {value}")
    print()

def run(log=False):
    info = collect_system_info()

    display_system_info(info)

    if log:
        log_info(info)
        print("System information logged.")

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Display system information."
    )

    parser.add_argument(
        "--log",
        action="store_true",
        help="Log system information to file"
    )

    return parser.parse_args()

def run_interactive():
    print("System Information Tool")

    choice = input("Log output to file? (y/n): ").strip().lower()

    log = choice == "y"

    run(log)

def main():
    args = parse_arguments()
    run(log=args.log)

if __name__ == "__main__":
    main()


# FUTURE IMPROVEMENTS
# live monitoring mode (refresh loop)
# network info (IP, interfaces)
# process listing
# export to JSON
# cross-platform normalization improvements