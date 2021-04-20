import sqlite3
import pathlib
import datetime

def connect():
    path = str(pathlib.Path(__file__).parent.absolute())
    return sqlite3.connect(path + "/database.db")
    # cara pake di main: connection = database.connect()

def createTables(connection):
    # id | date | matkul | jenis | deskripsi | 
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY AUTOINCREMENT, deadline DATE, matkul TEXT, jenis TEXT, deskripsi TEXT)")

def addTask(connection, deadline, matkul, jenis, deskripsi):
    # Poin 1
    # asumsi: deadline adalah string formatnya dd/mm/yyyy atau dd-mm-yyyy
    day = int(deadline[0:2])
    month = int(deadline[3:5])
    year = int(deadline[6:10]) 
    tanggal = datetime.date(year, month, day)

    with connection:
        connection.execute('''
            INSERT INTO task(deadline, matkul, jenis, deskripsi)
            VALUES(?,?,?,?)
        ''', (tanggal, matkul, jenis, deskripsi))

def getTaskAll(connection):
    # Poin 2a
    with connection:
        return connection.execute('''
            SELECT * FROM task
        ''').fetchall()

def getTaskByPeriod(connection, date1, date2):
    # Poin 2b
    day1 = int(date1[0:2])
    month1 = int(date1[3:5])
    year1 = int(date1[6:10]) 
    tanggal1 = datetime.date(year1, month1, day1)
    day2 = int(date2[0:2])
    month2 = int(date2[3:5])
    year2 = int(date2[6:10]) 
    tanggal2 = datetime.date(year2, month2, day2)

    with connection:
        return connection.execute('''
            SELECT * FROM task
            WHERE deadline >= ? AND deadline <= ?
        ''', (tanggal1, tanggal2))

def getTaskByType(connection, jenis):
    # Poin 2c
    with connection:
        return connection.execute('''
            SELECT * FROM task
            WHERE jenis = ?
        ''', (jenis,))

def getTaskByMatkulType(connection, matkul, jenis):
    # Poin 3
    with connection:
        return connection.execute('''
            SELECT * FROM task
            WHERE matkul = ? AND jenis = ?
        ''', (matkul, jenis))

def updateTaskDeadline(connection, id, deadline):
    # Poin 4
    day = int(deadline[0:2])
    month = int(deadline[3:5])
    year = int(deadline[6:10]) 
    tanggal = datetime.date(year, month, day)
    with connection:
        connection.execute('''
            UPDATE task
            SET deadline = ?
            WHERE id = ?
        ''', (tanggal, id))

def deleteTask(connection, id):
    # Poin 5
    with connection:
        connection.execute('''
            DELETE FROM task
            WHERE id = ?
        ''', (id,))

