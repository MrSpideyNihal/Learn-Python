"""Extract headings from markdown text."""
import re

def extract_headings(text):
    """Return a list of extracted headings."""
    headings = []
    for line in text.split("\n"): """Skip empty lines and leading/trailing whitespace."""
        line = line.strip()
        if line.startswith("# "):
            heading = re.sub(r"^# (.*)$", r'"\1"', line)
            headings.append(heading)
    return headings

if __name__ == "__main__":
    text = """
    # Heading 1
    # ======
    This is a heading.
    
    # Heading 2
    # ---------
    This is another heading.
    """
    print(extract_headings(text))"