from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_perpustakaan"
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def index():
    cursor.execute("SELECT * FROM buku")
    buku = cursor.fetchall()
    return render_template('index.html', buku=buku)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah_buku():
    if request.method == 'POST':
        judul = request.form['judul']
        penulis = request.form['penulis']
        tahun_terbit = request.form['tahun_terbit']
        isbn = request.form['isbn']
        
        cursor.execute("INSERT INTO buku (judul, penulis, tahun_terbit, isbn) VALUES (%s, %s, %s, %s)",
                       (judul, penulis, tahun_terbit, isbn))
        db.commit()
        
        return redirect(url_for('index'))
    return render_template('tambah.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_buku(id):
    if request.method == 'POST':
        judul = request.form['judul']
        penulis = request.form['penulis']
        tahun_terbit = request.form['tahun_terbit']
        isbn = request.form['isbn']
        
        cursor.execute("UPDATE buku SET judul=%s, penulis=%s, tahun_terbit=%s, isbn=%s WHERE id=%s",
                       (judul, penulis, tahun_terbit, isbn, id))
        db.commit()
        
        return redirect(url_for('index'))
    
    cursor.execute("SELECT * FROM buku WHERE id=%s", (id,))
    buku = cursor.fetchone()
    return render_template('edit.html', buku=buku)

@app.route('/hapus/<int:id>')
def hapus_buku(id):
    cursor.execute("DELETE FROM buku WHERE id=%s", (id,))
    db.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
    
