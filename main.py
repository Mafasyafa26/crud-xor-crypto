from koneksi import get_connection
from utils import load_key, encrypt_to_hex, decrypt_from_hex
import setup_db

def tambah_data():
    nama = input("Nama: ")
    data = input("Data rahasia: ")

    key = load_key()
    encrypted = encrypt_to_hex(data, key)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data_rahasia (nama, ciphertext) VALUES (%s, %s)", (nama, encrypted))
    conn.commit()

    print("Data berhasil disimpan!")
    cursor.close()
    conn.close()

def lihat_enkripsi():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data_rahasia")
    data = cursor.fetchall()

    print("\n=== DATA TERSIMPAN (CIPHER) ===")
    for row in data:
        print(f"{row[0]} | {row[1]} | {row[2]}")

    cursor.close()
    conn.close()

def lihat_dekripsi():
    pwd = input("Masukkan password admin: ")
    if pwd != load_key():
        print("Password salah!")
        return

    key = load_key()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data_rahasia")
    data = cursor.fetchall()

    print("\n=== DATA ASLI (DECRYPTED) ===")
    for row in data:
        decrypted = decrypt_from_hex(row[2], key)
        print(f"{row[0]} | {row[1]} | {decrypted}")

    cursor.close()
    conn.close()

def menu():
    setup_db.setup_database()

    while True:
        print("""
===== MENU =====
1. Tambah Data
2. Lihat Ciphertext
3. Lihat Data Asli
4. Keluar
""")
        choice = input("Pilih: ")

        if choice == "1":
            tambah_data()
        elif choice == "2":
            lihat_enkripsi()
        elif choice == "3":
            lihat_dekripsi()
        elif choice == "4":
            break
        else:
            print("Pilihan salah!")

if __name__ == "__main__":
    menu()
