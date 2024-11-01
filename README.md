# Tugas_Socket_Programming

# SockAtuh
SockAtuh adalah aplikasi chat sederhana berbasis UDP yang dibuat menggunakan library `socket` di Python. Aplikasi ini memungkinkan beberapa klien untuk bergabung ke dalam chatroom, dengan melakukan autentikasi dengan username dan password, serta mengirim pesan ke semua klien lain melalui server.

## Main Features
- **Koneksi Multi-Klien**: Mendukung beberapa klien untuk bergabung ke dalam satu ruang obrolan secara bersamaan, memungkinkan komunikasi grup secara real-time.
- **Autentikasi Pengguna**: Setiap klien harus memilih username yang unik dan memasukkan password yang benar untuk bergabung dalam chatroom, memberikan tingkat keamanan dasar.
- **Penyiaran Pesan (Broadcasting)**: Pesan yang dikirim oleh seorang klien akan diteruskan oleh server ke semua klien lain yang sudah terhubung, memungkinkan obrolan grup.
- **Penanganan Username Duplikat**: Server akan memeriksa apakah username yang dipilih oleh klien sudah digunakan. Jika sudah, klien akan diminta untuk memilih username lain.

## Project
- `server.py`: Program server yang menangani koneksi klien, memvalidasi username dan password, serta meneruskan pesan ke klien yang sudah bergabung.
- `client.py`: Program klien yang menghubungkan ke server, memungkinkan pengguna memasukkan username dan password, serta mengirim dan menerima pesan dalam ruang obrolan.

## How it Works
### Requirements

## How to Run
### Server
1. **Menjalankan Server**: Jalankan server dengan menjalankan `server.py`. Server akan meminta Anda untuk memasukkan alamat IP dan port.

   ```bash
   python server.py
