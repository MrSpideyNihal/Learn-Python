"""Grade calculator."""
import statistics

def calculate_grades(grades):
    """Return average grade, median grade and number of students."""
    return {'average': statistics.mean(grades), 'median': statistics.median(grades), 'count': len(grades)}

if __name__ == "__main__":
    grades = [85, 90, 78, 92, 88, 76]
    print(calculate_grades(grades))
