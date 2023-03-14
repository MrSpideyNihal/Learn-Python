"""Parse URLs using regex."""
import re

def parse_url(url):
    """Extract protocol, host, and path from a URL."""
    pattern = r"^(?:https?|ftp)(://)?([^/]+)(/.*)?$"
    match = re.match(pattern, url)
    if match:
        return {'protocol': match.group(1), 'host': match.group(2), 'path': match.group(3)}
    else:
        return None

if __name__ == "__main__":
    urls = ["http://example.com/path", "ftp://example.org"]
    for url in urls:
        print(parse_url(url))