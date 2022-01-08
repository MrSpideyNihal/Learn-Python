"""Calculate and display a student's grade based on their percentage."""
import math

def calculate_grade(percentage):
    """Return the corresponding letter grade for the given percentage."""
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

if __name__ == "__main__":
    x = int(input("Enter the student's percentage: "))
    print(f"Grade: {calculate_grade(x)}")