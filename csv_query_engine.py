"""CSV query engine."""
import csv

def QueryEngine():
    """CSV query engine class."""
    class Engine:
        def __init__(self, filename):
            self.filename = filename

        def query(self, column, value):
            with open(self.filename, 'r') as file:
                reader = csv.DictReader(file)
                return [row for row in reader if row[column] == str(value)]

    return Engine

if __name__ == "__main__":
    engine = QueryEngine('test.csv')
    print(engine.query('Name', 'John'))
