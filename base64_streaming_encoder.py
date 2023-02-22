"""Base64 encode and stream data."""
import base64

def encode_and_stream(data):
    """Return a generator that yields encoded data in chunks of 64 characters."""
    chunk_size = 64
    for i in range(0, len(data), chunk_size):
        yield base64.b64encode(data[i:i+chunk_size].encode()).decode()

if __name__ == "__main__":
    data = b'Hello World!'
    encoded_stream = encode_and_stream(data)
    for chunk in encoded_stream:
        print(chunk)
