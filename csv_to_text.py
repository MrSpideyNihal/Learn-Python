"""Convert CSV to text."""
import csv

def convert_csv_to_text(csv_file):
    """Read a CSV file and generate a text report."""
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is not None:
            print(', '.join(header))
        for row in reader:
            print(', '.join(row))

if __name__ == "__main__":
    convert_csv_to_text('example.csv')
