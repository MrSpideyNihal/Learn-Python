"""Caesar cipher encoder and decoder."""
def caesar_encrypt(plain_text, shift):
    """Shift the characters of the input string by the specified amount."""
    return ''.join(chr(ord(c) + shift) if c.isalpha() else c for c in plain_text)

def caesar_decrypt(cipher_text, shift):
    """Shift the characters of the input string back to their original positions."""
    return ''.join(chr(ord(c) - shift) if c.isalpha() else c for c in cipher_text)

if __name__ == "__main__":
    while True:
        user_input = input("Enter a message or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        elif user_input.startswith('d '):
            plain_text = caesar_decrypt(user_input[2:], 3)
            print(f"Decrypted: {plain_text}"
        else:
            encrypted = caesar_encrypt(user_input, 3)
            print(f"Encrypted: {encrypted}"
