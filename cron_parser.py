"""Parse and validate cron expressions."""
import re

def parse_cron(expression):
    """Return a dictionary representing the parsed cron expression."""
    parts = re.split(r'([0-9/]*)', expression)
    if len(parts) != 6:
        raise ValueError('Invalid cron format')
    return {
        'minute': int(parts[1]),
        'hour': int(parts[2]),
        'day_of_month': int(parts[3]),
        'month': int(parts[4]),
        'day_of_week': int(parts[5])
    }

if __name__ == "__main__":
    print(parse_cron('0 12 * * 1'))
