import subprocess
import platform
import time
import argparse

# default host to monitor
DEFAULT_HOST = "8.8.8.8"

# default delay
DEFAULT_INTERVAL = 2

# default number of checks
DEFAULT_COUNT = None

# log file (if logging enabled)
LOG_FILE = "network_monitor_log.txt"

def get_ping_command(host):
    system = platform.system()

    if system == "Windows":
        return ["ping", "-n", "1", host]
    else:
        return ["ping", "-c", "1", host]


def ping_host(host):
    command = get_ping_command(host)

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return result.returncode == 0

    except Exception:
        return False

from datetime import datetime


def format_status(success):
    return "UP" if success else "DOWN"


def log_status(host, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"[{timestamp}] {host} - {status}\n")


def monitor_host(host, interval, count=None, log=False):
    success_count = 0
    failure_count = 0
    iteration = 0

    print(f"\nMonitoring: {host}\n")

    while True:
        iteration += 1

        # ping
        success = ping_host(host)
        status = format_status(success)

        # print result
        print(f"[{iteration}] {status}")

        # log
        if log:
            log_status(host, status)

        # update counters
        if success:
            success_count += 1
        else:
            failure_count += 1

        # stop if count reached
        if count is not None and iteration >= count:
            break

        # wait before next ping
        time.sleep(interval)

    return success_count, failure_count


# function: display_summary(success_count, failure_count)
#   print:
#       total checks
#       successes
#       failures
#       uptime percentage

# function: parse_arguments()
#   arguments:
#       host (default: google.com)
#       interval (seconds)
#       count (optional number of pings)
#       --log (optional logging flag)


# function: run(host, interval, count=None, log=False)
#   validate inputs
#   call monitor_host
#   display summary


# function: run_interactive()
#   prompt user for:
#       host
#       interval
#       count (optional)
#       logging preference
#   apply defaults if blank
#   call run()


# function: main()
#   parse CLI arguments
#   call run()


# if __name__ == "__main__":
#   main()

# FUTURE IMPROVEMENTS
# multiple host monitoring
# latency measurement (ms)
# graphing uptime over time
# alerting (beep/email on failure)
# threading for concurrent monitoring
# continuous daemon mode