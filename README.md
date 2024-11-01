# Tugas_Socket_Programming

# SockAtuhChat
SockAtuhChat adalah aplikasi chat sederhana berbasis UDP yang dibuat menggunakan library `socket` di Python. Aplikasi ini memungkinkan beberapa klien untuk bergabung ke dalam chatroom, dengan melakukan autentikasi dengan username dan password, serta mengirim pesan ke semua klien lain melalui server.

Disusun oleh: Nadia Apsarini Baizal(18223065) dan Audy Alicia Renatha Tirayoh(18223097)

## Main Features
- **Koneksi Multi-Klien**: Mendukung beberapa klien untuk bergabung ke dalam satu ruang obrolan secara bersamaan, memungkinkan komunikasi grup secara real-time.
- **Autentikasi Pengguna**: Setiap klien harus memilih username yang unik dan memasukkan password yang benar untuk bergabung dalam chatroom, memberikan tingkat keamanan dasar.
- **Penyiaran Pesan (Broadcasting)**: Pesan yang dikirim oleh seorang klien akan diteruskan oleh server ke semua klien lain yang sudah terhubung, memungkinkan obrolan grup.
- **Penanganan Username Duplikat**: Server akan memeriksa apakah username yang dipilih oleh klien sudah digunakan. Jika sudah, klien akan diminta untuk memilih username lain.

## Project
- `server.py`: Program server yang menangani koneksi klien, memvalidasi username dan password, serta meneruskan pesan ke klien yang sudah bergabung.
- `client.py`: Program klien yang menghubungkan ke server, memungkinkan pengguna memasukkan username dan password, serta mengirim dan menerima pesan dalam ruang obrolan.

## How it Works
### Server
1. Server mendengarkan pesan UDP yang masuk dari klien.
2. Klien pertama-tama divalidasi berdasarkan username dan password:
   - Username: Setiap klien harus memilih username yang unik. Jika username sudah digunakan, server akan memberi tahu klien untuk memilih username lain.
   - Password: Setiap klien harus memasukkan password yang benar (juara dalam contoh ini) untuk bergabung ke dalam ruang obrolan.
3. Setelah validasi, klien dapat mengirim pesan ke ruang obrolan.
4. Server menampilkan pesan yang dikirim oleh klien dan meneruskannya ke semua klien yang terhubung kecuali pengirim.

### Client
1. Klien pertama-tama terhubung ke server menggunakan alamat IP dan port.
2. Kemudian, klien melewati proses autentikasi dua langkah:
   - Langkah 1: Memasukkan username yang unik. Jika username valid, server akan merespon dengan "Username valid!".
   - Langkah 2: Memasukkan password ruang obrolan. Jika password benar, server akan merespon dengan "Berhasil bergabung!".
- Setelah berhasil, klien dapat mengirim dan menerima pesan.

## How to Run
### Requirements
- Python 3.x harus sudah terpasang pada komputer.
- Klien dan server dapat dijalankan di komputer yang berbeda selama berada dalam satu jaringan yang sama.

### Server
1. Jalankan server (`server.py`) dengan perintah:
   ```bash
   python server.py
2.  Masukkan alamat IP dan Port dimana server akan dijalankan.
3. Server akan menampilkan pesan yang mengonfirmasi bahwa server berjalan dan siap menerima koneksi.

### Client
1. Jalankan client (`client.py`) dengan perintah:
   ```bash
   python client.py
2.  Masukkan alamat IP dan Port dimana server telah dijalankan.
