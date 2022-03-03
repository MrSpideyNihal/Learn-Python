"""Check if a year is a leap year."""
import datetime

def is_leap(year):
    """Return True if the year is a leap year, False otherwise."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == "__main__":
    year = int(input("Enter a year: "))
    if is_leap(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
