import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_perpustakaan"
)

cursor = db.cursor()
sql = """CREATE TABLE buku (
    id INT AUTO_INCREMENT PRIMARY KEY,
    judul VARCHAR(255) NOT NULL,
    penulis VARCHAR(255) NOT NULL,
    tahun_terbit INT,
    isbn VARCHAR(20) UNIQUE
)"""

cursor.execute(sql)
print("table buku berhasil dibuat")