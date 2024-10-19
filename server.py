import socket
import threading

# Global list to store client addresses
clients = []

def handle_client(server_socket, client_address):
    while True:
        try:
            message, _ = server_socket.recvfrom(1024)
            print(f"Message from {client_address}: {message.decode('utf-8')}")

            # Forward the message to other clients
            for client in clients:
                if client != client_address:
                    server_socket.sendto(message, client)

        except Exception as e:
            print(f"Error: {e}")
            clients.remove(client_address)
            break

def start_server():
    # Server information
    host = '172.20.10.7'  # Localhost
    port = 12345        # Arbitrary non-privileged port

    # Create UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"Server started on {host}:{port}")

    while True:
        message, client_address = server_socket.recvfrom(1024)
        if client_address not in clients:
            clients.append(client_address)
            print(f"New client connected: {client_address}")
            # Start a new thread to handle communication
            thread = threading.Thread(target=handle_client, args=(server_socket, client_address))
            thread.start()

if __name__ == "__main__":
    start_server()
