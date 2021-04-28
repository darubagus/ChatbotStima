import sqlite3
import pathlib
import datetime

def connect():
    # Melakukan sinkronisasi database dalam sebuah variabel
    path = str(pathlib.Path(__file__).parent.absolute())
    return sqlite3.connect(path + "/database.db")

def createTables(connection):
    # Membuat tabel task dengan atribut id, deadline, matkul, jenis, deskripsi
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY AUTOINCREMENT, deadline DATE, matkul TEXT, jenis TEXT, deskripsi TEXT)")

def addTask(connection, d, m, y, matkul, jenis, deskripsi):
    # Poin 1
    # Menambahkan task baru dari parameter yang dimasukkan
    day = int(d)
    month = int(m)
    year = int(y) 
    tanggal = datetime.date(year, month, day)

    with connection:
        connection.execute('''
            INSERT INTO task(deadline, matkul, jenis, deskripsi)
            VALUES(?,?,?,?)
        ''', (tanggal, matkul, jenis, deskripsi))

def getTaskAll(connection):
    # Poin 2a
    # Melakukan fetch semua instance data dari database task
    with connection:
        return connection.execute('''
            SELECT * FROM task
        ''').fetchall()

def getTaskByPeriod(connection, d1, m1, y1, d2, m2, y2):
    # Poin 2b
    # Melakukan fetch instance data dari database task pada suatu interval waktu
    day1 = int(d1)
    month1 = int(m1)
    year1 = int(y1) 
    tanggal1 = datetime.date(year1, month1, day1)
    day2 = int(d2)
    month2 = int(m2)
    year2 = int(y2) 
    tanggal2 = datetime.date(year2, month2, day2)

    with connection:
        return connection.execute('''
            SELECT * FROM task
            WHERE deadline >= ? AND deadline <= ?
        ''', (tanggal1, tanggal2)).fetchall()

def getTaskByExactDate(connection, d1, m1, y1):
    # Poin 2b
    # Melakukan fetch instance data dari database task pada suatu waktu
    day1 = int(d1)
    month1 = int(m1)
    year1 = int(y1) 
    tanggal1 = datetime.date(year1, month1, day1)

    with connection:
        return connection.execute('''
            SELECT * FROM task
            WHERE deadline = ? 
        ''', (tanggal1,)).fetchall()

def getTaskByType(connection, jenis):
    # Poin 2c
    # Melakukan fetch instance data dari database task sesuai dengan jenis task tertentu
    with connection:
        return connection.execute('''
            SELECT * FROM task
            WHERE jenis = ?
        ''', (jenis,)).fetchall()

def getTaskByMatkul(connection, matkul):
    # Poin 3
    # Melakukan fetch instance data dari database task sesuai dengan kode mata kuliah yang dicari
    with connection:
        return connection.execute('''
            SELECT * FROM task
            WHERE matkul = ? 
        ''', (matkul,)).fetchall()

def getTaskByMatkulType(connection, matkul, jenis):
    # Poin 3
    # Melakukan fetch instance data dari database task sesuai dengan kode mata kuliah dan jenis task tertentu
    with connection:
        return connection.execute('''
            SELECT * FROM task
            WHERE matkul = ? AND jenis = ?
        ''', (matkul, jenis)).fetchall()

def updateTaskDeadline(connection, id, d, m, y,):
    # Poin 4
    # Update deadline dari suatu task
    day = int(d)
    month = int(m)
    year = int(y) 
    tanggal = datetime.date(year, month, day)
    with connection:
        connection.execute('''
            UPDATE task
            SET deadline = ?
            WHERE id = ?
        ''', (tanggal, int(id)))

def deleteTask(connection, id):
    # Poin 5
    # Menghapus sebuah instance task dari database
    with connection:
        connection.execute('''
            DELETE FROM task
            WHERE id = ?
        ''', (int(id),))

def getMaxId(connection):
    # Mengambil Id maksimum dari database task
    with connection:
        return connection.execute('''
            SELECT max(id)
            FROM task
        ''').fetchall()[0][0]