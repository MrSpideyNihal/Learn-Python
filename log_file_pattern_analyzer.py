"""Analyze log files."""
import re

def analyze_log_files(logs):
    """Return the number of occurrences for each log level in 'logs'."""
    log_levels = {'INFO': 0, 'WARNING': 1, 'ERROR': 2}
    log_counts = {level: 0 for level in log_levels}
    pattern = re.compile(r'^(INFO|WARNING|ERROR).*')
    for log in logs:
        match = pattern.match(log)
        if match:
            log_level = match.group(1)
            log_counts[log_level] += 1
    return {level: count for level, count in sorted(log_counts.items())}

if __name__ == "__main__":
    logs = ['2022-01-01 12:00 INFO Something happened.', '2022-01-02 13:00 WARNING Something else happened.', '2022-01-03 14:00 ERROR Something went wrong.']
    print(analyze_log_files(logs))