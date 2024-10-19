import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message, _ = client_socket.recvfrom(1024)
            print(message.decode('utf-8'))
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def start_client():
    # Server information
    server_ip = '127.0.0.1'  # Ganti dengan IP server
    server_port = 12345      # Port yang sama dengan server

    # Create UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    username = input("Enter your username: ")
    password = input("Enter the chatroom password: ")  # Password tidak divalidasi saat ini

    # Initial message to join the chatroom
    client_socket.sendto(f"{username} has joined the chat".encode('utf-8'), (server_ip, server_port))

    # Start a thread to receive messages from server
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        message = input()
        if message.lower() == 'exit':
            client_socket.sendto(f"{username} has left the chat".encode('utf-8'), (server_ip, server_port))
            break
        client_socket.sendto(f"{username}: {message}".encode('utf-8'), (server_ip, server_port))

    client_socket.close()

if __name__ == "__main__":
    start_client()