"""Convert timezone from UTC to specified timezone."""
import datetime

def convert_to_local(time, tz):  # noqa: F811
    return datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S').astimezone(eval(f'datetime.timezone({tz})'))

def convert_timezone():
    """Convert timezone from UTC to specified timezone."""
    time = '2022-01-01 12:00:00'
    tz = input('Enter timezone (e.g. US/Eastern): ')
    print(convert_to_local(time, tz))

if __name__ == "__main__":
    convert_timezone()
