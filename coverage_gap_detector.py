"""Detect gaps in code coverage."""
import collections

def find_gaps(covered_lines, total_lines):
    """Find lines with no test coverage."""
    return [line for line in range(total_lines) if line not in covered_lines]

if __name__ == "__main__":
    covered_lines = list(range(10))
    total_lines = 15
    gaps = find_gaps(covered_lines, total_lines)
    print(f"Gaps: {gaps}")