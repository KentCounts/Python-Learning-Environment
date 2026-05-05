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


def display_summary(success_count, failure_count):
    total = success_count + failure_count

    # avoid division by zero
    if total == 0:
        uptime_percent = 0.0
    else:
        uptime_percent = (success_count / total) * 100

    print("\n=== Monitoring Summary ===\n")
    print(f"Total checks: {total}")
    print(f"Successes: {success_count}")
    print(f"Failures: {failure_count}")
    print(f"Uptime: {uptime_percent:.2f}%\n")

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Monitor network uptime by pinging a host."
    )

    parser.add_argument(
        "host",
        nargs="?",
        default=DEFAULT_HOST,
        help=f"Host to monitor (default: {DEFAULT_HOST})"
    )

    parser.add_argument(
        "--interval",
        type=float,
        default=DEFAULT_INTERVAL,
        help=f"Seconds between pings (default: {DEFAULT_INTERVAL})"
    )

    parser.add_argument(
        "--count",
        type=int,
        default=DEFAULT_COUNT,
        help="Number of pings to send (default: infinite)"
    )

    parser.add_argument(
        "--log",
        action="store_true",
        help="Log results to file"
    )

    return parser.parse_args()


def run(host, interval, count=None, log=False):
    # basic validation
    if interval <= 0:
        print("Error: Interval must be greater than 0.")
        return

    if count is not None and count <= 0:
        print("Error: Count must be greater than 0.")
        return

    print(f"Starting monitor for: {host}")
    print(f"Interval: {interval} seconds")
    print(f"Count: {'infinite' if count is None else count}")
    print(f"Logging: {'enabled' if log else 'disabled'}")

    success_count, failure_count = monitor_host(
        host, interval, count=count, log=log
    )

    display_summary(success_count, failure_count)


def run_interactive():
    print("Network Monitor")

    host = input(f"Enter host (default: {DEFAULT_HOST}): ").strip()
    interval = input(f"Enter interval in seconds (default: {DEFAULT_INTERVAL}): ").strip()
    count = input("Enter number of pings (leave blank for infinite): ").strip()
    log_choice = input("Enable logging? (y/n): ").strip().lower()

    # apply defaults
    if not host:
        host = DEFAULT_HOST

    if not interval:
        interval = DEFAULT_INTERVAL
    else:
        try:
            interval = float(interval)
        except ValueError:
            print("Invalid interval. Using default.")
            interval = DEFAULT_INTERVAL

    if not count:
        count = None
    else:
        try:
            count = int(count)
        except ValueError:
            print("Invalid count. Using infinite.")
            count = None

    log = log_choice == "y"

    run(host, interval, count, log)


def main():
    args = parse_arguments()
    run(args.host, args.interval, args.count, args.log)

if __name__ == "__main__":
    main()

# FUTURE IMPROVEMENTS
# multiple host monitoring
# latency measurement (ms)
# graphing uptime over time
# alerting (beep/email on failure)
# threading for concurrent monitoring
# continuous daemon mode