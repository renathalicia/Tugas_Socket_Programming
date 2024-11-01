import socket
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import simpledialog, messagebox

# Konfigurasi client
ip = input("Masukkan IP server: ")
port = int(input("Masukkan port server: "))
buffer = 1024

# Membuat socket UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Fungsi untuk menerima pesan dari server
def receive_messages():
    while True:
        try:
            data, _ = client.recvfrom(buffer)
            message = data.decode()
            chat_log.config(state="normal")
            chat_log.insert(tk.END, message + "\n")
            chat_log.config(state="disabled")
            chat_log.yview(tk.END)
        except:
            break

# Fungsi untuk mengirim pesan ke server
def send_message():
    message = message_entry.get()
    if message:
        client.sendto(message.encode(), (ip, port))
        message_entry.delete(0, tk.END)

# Fungsi untuk login dengan username dan password
def login():
    global username
    username = simpledialog.askstring("Login", "Masukkan username:")
    password = simpledialog.askstring("Password", "Masukkan password:", show="*")

    client.sendto(f"Username:{username}".encode(), (ip, port))
    data, _ = client.recvfrom(buffer)
    response = data.decode()

    if response == "Username valid!":
        client.sendto(f"Password:{password}".encode(), (ip, port))
        data, _ = client.recvfrom(buffer)
        response = data.decode()

        if response == "Berhasil bergabung!":
            login_frame.pack_forget()
            chat_frame.pack(fill="both", expand=True)
            threading.Thread(target=receive_messages, daemon=True).start()
        else:
            messagebox.showerror("Error", "Password salah!")
    else:
        messagebox.showerror("Error", "Username sudah dipakai atau tidak dikenali!")

# Inisialisasi GUI
client_window = tk.Tk()
client_window.title("SockAtuhChat")
client_window.geometry("400x400")

# Login frame
login_frame = tk.Frame(client_window)
login_frame.pack(fill="both", expand=True)

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack(pady=20)

# Chat frame
chat_frame = tk.Frame(client_window)

chat_log = ScrolledText(chat_frame, state="disabled", wrap="word")
chat_log.pack(pady=10, padx=10, fill="both", expand=True)

message_entry = tk.Entry(chat_frame)
message_entry.pack(fill="x", padx=10, pady=5)

send_button = tk.Button(chat_frame, text="Send", command=send_message)
send_button.pack(pady=5)

client_window.mainloop()
