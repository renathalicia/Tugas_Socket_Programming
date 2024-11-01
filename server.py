import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# Konfigurasi server
ip = input("Masukkan IP server: ")
port = int(input("Masukkan port server: "))
buffer = 1024
clients = {}
pending = {}

# Membuat socket UDP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((ip, port))

# Fungsi untuk broadcast pesan ke client
def broadcast_message(message, sender_username):
    for username, addr in clients.items():
        if username != sender_username:
            server.sendto(message.encode(), addr)

# Fungsi untuk menerima dan menangani pesan dari client
def receive_messages():
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
                        log_message(f"Client {username} bergabung dari {client_addr}")
                        del pending[client_addr]
                        server.sendto("Berhasil bergabung!".encode(), client_addr)
                    else:
                        server.sendto("Password salah! Silakan coba lagi.".encode(), client_addr)
        
        else:
            sender_username = [name for name, addr in clients.items() if addr == client_addr][0]
            log_message(f"Pesan dari {sender_username}: {message}")
            broadcast_message(f"{sender_username}: {message}", sender_username)

# Fungsi untuk log pesan di GUI
def log_message(message):
    chat_log.config(state="normal")
    chat_log.insert(tk.END, message + "\n")
    chat_log.config(state="disabled")
    chat_log.yview(tk.END)

# Inisialisasi GUI
server_window = tk.Tk()
server_window.title("Server SockAtuhChat")
server_window.geometry("400x300")

chat_log = ScrolledText(server_window, state="disabled", wrap="word")
chat_log.pack(pady=10, padx=10, fill="both", expand=True)

log_message(f"Server berjalan di {ip}:{port}")

# Jalankan thread untuk menerima pesan
receive_thread = threading.Thread(target=receive_messages)
receive_thread.daemon = True
receive_thread.start()

server_window.mainloop()
