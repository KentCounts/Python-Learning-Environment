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

# =========================
# HELPER FUNCTIONS
# =========================

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


# function: format_status(success)
#   return formatted string:
#       "UP" or "DOWN"

# function: log_status(host, status)
#   append timestamped status to log file
#   example:
#       [2026-04-30 12:00:00] google.com - UP

# function: monitor_host(host, interval, count=None)
#   initialize counters:
#       success_count
#       failure_count
#
#   loop:
#       ping host
#       determine status (UP/DOWN)
#       print result
#       log result (optional)
#       update counters
#
#       if count is set:
#           stop after count iterations
#
#       sleep(interval)


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