"""Get IP address information."""
import socket

def get_ip_info():
    """Return IP address details."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return s.gethostname(), s.gethostbyaddr(s.gethostname())[2]
    except Exception as e:
        return 'Error: ' + str(e)

if __name__ == "__main__":
    print(get_ip_info())
