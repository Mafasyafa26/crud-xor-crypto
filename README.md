# Aplikasi CRUD dengan Enkripsi XOR Stream Cipher

Aplikasi ini adalah simulasi CRUD sederhana yang menggunakan teknik enkripsi simetris XOR Stream Cipher. Data sensitif yang disimpan ke dalam database MySQL akan dienkripsi terlebih dahulu dalam bentuk hexadecimal sehingga tidak dapat dibaca tanpa kunci.

Tugas Sesi 6 — Implementasi Kriptografi

---

## A. Struktur File

1. `main.py`        : Program utama, berisi menu CRUD.  
2. `koneksi.py`     : Mengatur koneksi ke database MySQL.  
3. `utils.py`       : Fungsi enkripsi XOR, dekripsi, dan pembacaan key.  
4. `setup_db.py`    : Script otomatis untuk membuat database dan tabel.  
5. `key.txt`        : File kunci untuk proses enkripsi dan dekripsi.  
6. `db_kriptografi.sql` : Dump database MySQL (struktur tabel).  

---

## B. Persyaratan Sistem

1. Python 3.x  
2. MySQL Server (XAMPP / Laragon / Workbench)  
3. Library Python: `mysql-connector-python`  

---

## C. Cara Instalasi dan Menjalankan

### Langkah 1: Install library  
Buka terminal / CMD, lalu jalankan:

```bash
pip install mysql-connector-python
```

### Langkah 2: Konfigurasi MySQL  
Buka file `koneksi.py` dan `setup_db.py`, lalu sesuaikan username/password MySQL pada komputer.

Contoh:

```python
user="root"
password=""
```

### Langkah 3: Buat file key  
Buat file bernama `key.txt` dalam folder proyek, lalu isi dengan satu password.

Contoh isi:

```
admin123
```

### Langkah 4: Jalankan aplikasi

```bash
python main.py
```

Jika pertama kali dijalankan, sistem akan membuat database dan tabel secara otomatis.

---

## D. Panduan Penggunaan

1. **Tambah Data**  
   Menginput nama dan data sensitif. Data akan dienkripsi dan disimpan dalam bentuk hex.

2. **Lihat Ciphertext**  
   Menampilkan data langsung dari database dalam kondisi terenkripsi.

3. **Lihat Data Asli**  
   Membutuhkan password yang sama dengan isi file `key.txt`. Jika benar, data akan didekripsi.

4. **Hapus Data**  
   Penghapusan data memerlukan verifikasi password admin.

---

## E. Mekanisme Keamanan

* Algoritma menggunakan XOR Stream Cipher.  
* Data dienkripsi lalu dikonversi ke hexadecimal sebelum disimpan.  
* Kunci enkripsi dipisahkan melalui file `key.txt` sebagai simulasi penyimpanan aman.  
* Tanpa key, data tidak dapat didekripsi kembali.

---

## F. Dump Database

Project ini menyertakan file `db_kriptografi.sql` sebagai dump database MySQL.

Isi dump terdiri dari:

* Struktur tabel `data_rahasia`  
* Kolom `id`, `nama`, `ciphertext`  

Cara restore:

1. Buka phpMyAdmin  
2. Buat database baru bernama `db_kriptografi`  
3. Masuk ke menu Import  
4. Pilih file `db_kriptografi.sql`  
5. Klik Go  

---

Dibuat menggunakan Python dan MySQL Connector  
Oleh: Mafasyafa Annisa Zukhruff / 230401010036
