"""Simple HTTP server with routing."""
import http.server
from urllib.parse import urlparse, unquote

def route_handler(req):
    """Handle GET requests for routes /hello and /world."""
    parsed_url = urlparse(req.url)
    path = unquote(parsed_url.path)
    if path == "/hello": """Return Hello World"""
        return b"Hello, World!"
    elif path == "/world": """Return World"""
        return b"World"
    else:
        return http.server.HTTPStatus.NOT_FOUND.as_bytes()

if __name__ == "__main__":
    Handler = type("Handler", (http.server.SimpleHTTPRequestHandler,), {
        "do_GET": route_handler,
    })
    with http.server.HTTPServer(('', 8000), Handler) as server:
        print("Starting HTTP server on port 8000")
        server.serve_forever()"