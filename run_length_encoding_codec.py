"""Run-Length Encoding (RLE) codec."""
import collections

def rle_encode(data):
    """Return the RLE encoded string for 'data'."""
    if not data:
        return ''
    encoded = ''
    count = 1
    prev_char = data[0]
    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            encoded += str(count) + prev_char if count > 1 else prev_char
            prev_char = char
            count = 1
    encoded += str(count) + prev_char if count > 1 else prev_char
    return encoded

def rle_decode(encoded):
    """Return the original string for 'encoded' RLE encoding."""
    decoded = ''
    count = ''
    for char in encoded:
        if char.isdigit():
            count += char
        else:
            decoded += char * int(count)
            count = ''
    return decoded

if __name__ == "__main__":
    data = 'A' * 10 + 'B' * 5 + 'A' * 15
    encoded = rle_encode(data)
    print(encoded)
    decoded = rle_decode(encoded)
    print(decoded)