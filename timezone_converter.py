"""Convert timezone offset to hours and minutes."""
import datetime

def convert_offset(offset):
    """Return hours and minutes from timezone offset."""
    return str(int((offset / 60) % 24)).zfill(2), str(int(abs(offset) % 60)).zfill(2)

if __name__ == "__main__":
    offset = int(input("Enter timezone offset (in minutes): "))
    hours, minutes = convert_offset(offset)
    print(f"{hours}:{minutes}")
