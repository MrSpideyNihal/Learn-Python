"""Template engine for simple variable substitution."""
import re

def parse_template(template):
    """Parse template and replace placeholders."""
    return re.sub(r'\[(.*)\]', lambda m: m.group(1), template)

def render_template(template, vars):
    """Render template with variables."""
    return parse_template(template).format(**vars)

if __name__ == "__main__":
    print(render_template("Hello, {name}!", {'name': 'John'}))
