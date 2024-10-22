import socket
import threading

ip = input("Masukkan IP server: ")
port = int(input("Masukkan port server: "))
buffer = 1024

# Membuat socket UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Client input username
username = input("Masukkan username: ")

def receive():
    while True:
        try:
            data,_ = client.recvfrom(buffer)
            print(data.decode())
        except:
            break

# Mengecek apakah password sudah benar
password_correct = False
while not password_correct:
    password = input("Masukkan password chatroom: ")
    client.sendto(f"{username}:{password}".encode(), (ip, port))
    data, _ = client.recvfrom(buffer)
    response = data.decode()
    print(response)
    if response == "Berhasil bergabung!":
        password_correct = True

receive_thread = threading.Thread(target=receive)
receive_thread.start()

while True:
    message = input()
    client.sendto(message.encode(), (ip, port))