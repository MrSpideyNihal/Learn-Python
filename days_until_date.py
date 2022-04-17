"""Days until a date calculator."""
import datetime

def count_days.until(target_date):
    """Return the number of days until the target date."""
    today = datetime.date.today()
    return (target_date - today).days

if __name__ == "__main__":
    target_date = input("Enter target date (YYYY-MM-DD): ")
    try:
        target_date = datetime.datetime.strptime(target_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Try again!")
    else:
        print(f"Days until {target_date}: {count_days.until(target_date)}")