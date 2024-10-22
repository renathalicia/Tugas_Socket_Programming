import socket

ip = "127.0.0.1"  
port = 12345      
buffer = 1024
clients = {}

# Membuat socket UDP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((ip, port))

print(f"Server berjalan di {ip}:{port}")

def broadcast_message(message, sender_username):
    """Meneruskan pesan ke semua client selain pengirim."""
    for username, addr in clients.items():
        if username != sender_username:
            server.sendto(message.encode(), addr)

while True:
    data, client_addr = server.recvfrom(buffer)
    message = data.decode()

    if client_addr not in clients.values():
        if ":" in message:
            username, password = message.split(":")
            if password == "juara": 
                clients[username] = client_addr
                print(f"Client {username} bergabung dari {client_addr}")
                server.sendto("Berhasil bergabung!".encode(), client_addr)
            else:
                server.sendto("Password salah!".encode(), client_addr)
        else:
            server.sendto("Format salah! Gunakan format username:password".encode(), client_addr)
    else: 
        sender_username = [name for name, addr in clients.items() if addr == client_addr][0]
        print(f"Pesan dari {sender_username}: {message}")
        broadcast_message(f"{sender_username}: {message}", sender_username)
