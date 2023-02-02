"""Verify HMAC signatures."""
import hmac

def verify_hmac(message, signature, key):
    """Return True if the message is verified by the given HMAC signature using the 'key'."""
    return hmac.compare_digest(hmac.new(key.encode(), message.encode()).digest(), signature)

if __name__ == "__main__":
    message = b'Hello, World!' * 5
    key = b'secret_key'
    signature = hmac.new(key, message, digestmod='SHA256').digest()
    print(verify_hmac(message, signature, key))