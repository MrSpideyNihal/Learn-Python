"""Log rotation utility."""
import os
import datetime
from collections import deque

def rotate_log(filename):
    """Rotate log file to a new file and keep track of the last 10 logs."""
    if not os.path.exists(filename):
        return False
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    today = datetime.date.today().strftime("%Y-%m-%d")
    log_file = f"{filename}.log.{today}" if not os.path.exists(log_file) else None
    with open(log_file, 'w') as new_f:
        for line in lines[-10:]:
            new_f.write(line + '\n')
    return True

if __name__ == "__main__":
    print(rotate_log("log.txt"))
