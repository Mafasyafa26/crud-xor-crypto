import mysql.connector

def setup_database():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""   # XAMPP password selalu kosong
    )
    cursor = conn.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS db_kriptografi;")
    cursor.execute("USE db_kriptografi;")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data_rahasia (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nama VARCHAR(255),
            ciphertext TEXT
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Database dan tabel berhasil dibuat!")

if __name__ == "__main__":
    setup_database()
