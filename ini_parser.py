"""Parse and validate INI configuration files."""
import re

def parse_ini(input_str):
    """Return a dictionary representing the parsed INI configuration."""
    sections = {}
    current_section = None
    for line in input_str.split('
'):
        if line.startswith(';') or not line.strip():
            continue
        match = re.match(r'([A-Za-z0-9_]+)=(.*)', line)
        if match:
            key, value = match.groups()
            if current_section is None:
                raise ValueError('Invalid INI format')
            sections[current_section][key] = value
        else:
            match = re.match(r'([A-Za-z0-9_]+)', line)
            if match:
                current_section = match.group(1)
                sections[current_section] = {}
    return sections

if __name__ == "__main__":
    print(parse_ini('[section]
description=Hello, world!
[another_section]
some_key=some_value'))
