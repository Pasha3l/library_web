
import mysql.connector as koneksi
konek = koneksi.connect(host='localhost',user='root',passwd='')

if konek:
    print("berhasil")
else:
    print("gagal")
    
kursor = konek.cursor()
kursor.execute("CREATE DATABASE db_perpustakaan")
print('Database berhasil dibuat')
konek.close()


