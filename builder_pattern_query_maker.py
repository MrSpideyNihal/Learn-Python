"""A simple builder pattern to create SQL queries."""
class QueryBuilder:
    """A simple builder pattern for creating SQL queries."""
    def __init__(self):
        self.query = ''
        self.where_clause = ''

    def select(self, columns):
        """Add a SELECT clause to the query."""
        self.query += 'SELECT '
        for column in columns:
            self.query += f'{column}, '
        self.query = self.query[:-2] + ';
'
    def from_(self, table_name):
        """Add a FROM clause to the query."""
        self.query += f'FROM {table_name};
'
    def where(self, column, operator, value):
        """Add a WHERE clause to the query."""
        if not self.where_clause:
            self.where_clause = f'WHERE {column} {operator} {value};
'
    def build_query(self):
        """Build and return the SQL query."""
        if self.where_clause:
            self.query += self.where_clause
        return self.query

if __name__ == "__main__":
    builder = QueryBuilder()
    builder.select(['id', 'name'])
    builder.from_('users')
    builder.where('age', '>', 25)
    print(builder.build_query())
