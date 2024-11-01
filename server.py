import socket

ip = input("Masukkan IP server: ")
port = int(input("Masukkan port server: "))
buffer = 1024
clients = {} # Menyimpan client yang sudah valid
pending = {} # Menyimpan client sementara sebelum validasi password

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
        if message.startswith("Username:"):
            username = message.split(":")[1]

            if username in clients:
                server.sendto("Username sudah dipakai! Gunakan username lain.".encode(), client_addr)
            else:
                server.sendto("Username valid!".encode(), client_addr)
                pending[client_addr] = username


        elif message.startswith("Password:"):
            if client_addr in pending:
                username = pending[client_addr]
                password = message.split(":")[1]

                if password == "juara": 
                    clients[username] = client_addr
                    print(f"Client {username} bergabung dari {client_addr}")
                    del pending[client_addr]
                    server.sendto("Berhasil bergabung!".encode(), client_addr)
            
                else:
                    server.sendto("Password salah! Silakan coba lagi.".encode(), client_addr)
            
    else: 
        sender_username = [name for name, addr in clients.items() if addr == client_addr][0]
        print(f"Pesan dari {sender_username}: {message}")
        broadcast_message(f"{sender_username}: {message}", sender_username)
