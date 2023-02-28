"""Simple chat server using sockets."""
import socket

def handle_client(client_socket):
    """Handle a single client connection."""
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(f"Received: {message}")

if __name__ == "__main__":
    host = 'localhost'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Chat Server started on {host}:{port}")
    while True:
        client_socket, address = server_socket.accept()
        handle_client(client_socket)
