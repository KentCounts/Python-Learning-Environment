
# subprocess for running system ping command
# platform to detect OS (Windows vs Linux/Mac)
# time for delays between pings
# argparse for CLI

# default target host (e.g., "8.8.8.8" or "google.com")
# default ping interval (seconds)
# default number of pings (optional, or infinite)
# timeout settings (optional)

# function: get_ping_command(host)
#   return correct ping command depending on OS
#   Windows:
#       ping -n 1 host
#   Linux/Mac:
#       ping -c 1 host


# function: ping_host(host)
#   execute ping command using subprocess
#   return:
#       True if successful
#       False if failed


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