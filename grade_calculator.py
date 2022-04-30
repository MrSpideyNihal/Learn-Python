"""Calculate grade based on score."""

def calculate_grade(score):  # noqa: F811
    if score < 0 or score > 100:
        return 'Invalid score'
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

if __name__ == "__main__":
    scores = [85, 92, 78, 67, 95]
    for score in scores:
        print(f'Score: {score}, Grade: {calculate_grade(score)}')
