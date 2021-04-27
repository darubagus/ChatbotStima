import os
from flask import *
import sqlite3 as sql
from KMP import *
from Regex import *
from database import *

app = Flask(__name__)

# APP_ROUTE = os.path.dirname(os.path.abspath(__file__))

command = [
    'tambah', 'Tambah', # Menambah task baru (poin 1) 
    'update', 'Update', 'ubah', 'Ubah', 'diundur', 'Diundur', 'dimajukan', 'Dimajukan', # Update task (poin 4)
    'deadline', 'Deadline', # Melihat deadline (poin 2/3)
    'selesai', 'Selesai', # Selesai mengerjakan task (poin 5)
    'help', 'Help', 'lakukan', 'Lakukan', 'perintah', 'Perintah' # Menampilkan help (poin 6)
]

@app.route("/", methods = ['POST', 'GET'])
def index():
    connection = connect() # ini database
    chat = ["Selamat datang di jam-bot (red: jamboard), masukkan perintah anda"] # array buat nampung chat (string)
    if (request.method == 'POST'):
        query = request.form['query'] # variabel query di html
        chat.append(query) 
        for cmd in command:
            if (KMPStringMatch(query, cmd)):
                break

        if (cmd == 'tambah' or cmd == 'Tambah'):
            matkul = searchKodeMatkul(query)
            topik = searchTopik(query)
            tanggal = searchTanggal(query)
            jenis = searchJenis(query)
            if (matkul != None and topik != None and tanggal != None and jenis != None):
                if (isTanggalValid(tanggal[0])):
                    addTask(connection, tanggal[0][0], tanggal[0][1], tanggal[0][2], matkul, jenis, topik)
                    arr = getTaskAll(connection)
                    line = ""
                    #(ID: 1) 14/04/2021 - IF2211 - Tubes - String matching
                    # d, m, y, matkul, jenis, deskripsi
                    for el in arr:
                        line += "(ID: " + el[0] + ") " + el[1] + " - " + el[2] + " - " + el[3] + " - " + el[4] + "\n"
                    chat.append("[Task Berhasil Dicatat]\n" + line)
                else:
                    chat.append("Tanggal tidak valid")
            else:
                error = ""
                if (matkul == None):
                    error += "Tidak ada kode matkul\n"
                if (topik == None):
                    error += "Tidak ada topik tugas\n"
                if (tanggal == None):
                    error += "Tidak ada tanggal tugas\n"
                if (jenis == None):
                    error += "Tidak ada jenis tugas\n"   

                chat.append(error)    
        
        elif (cmd == 'deadline' or cmd == 'Deadline'):
            if():
                pass
            elif():
                pass
            else:
                pass

        elif (cmd == 'update' or cmd == 'Update' or cmd == 'ubah' or cmd == 'Ubah' or cmd == 'diundur' or cmd == 'Diundur' or cmd == 'dimajukan' or cmd == 'Dimajukan'):
            pass
        
        elif (cmd == 'selesai' or cmd == 'Selesai'):
            pass
        
        elif (cmd == 'help' or cmd == 'Help' or cmd == 'lakukan' or cmd == 'Lakukan' or cmd == 'perintah' or cmd == 'Perintah'):
            pass

        else:
            chat.append("Ngomong apa lo")


    return render_template("home.html")


def isTanggalValid(tanggal):
    if (tanggal[1] == '4' or tanggal[1] == 'April' or tanggal[1] == 'april'
    or tanggal[1] == '6' or tanggal[1] == 'Juni' or tanggal[1] == 'juni'
    or tanggal[1] == '9' or tanggal[1] == 'September' or tanggal[1] == 'september'
    or tanggal[1] == '11' or tanggal[1] == 'November' or tanggal[1] == 'november'):
        if (tanggal[0] == '31'):
            return False
    elif (tanggal[1] == '2' or tanggal[1] == 'Februari' or tanggal[1] == 'februari'):
        if (int(tanggal[2]) % 4 == 0):
            if (int(tanggal[2]) % 100 == 0):
                if (int(tanggal[2]) % 400 == 0):
                    if (int(tanggal[0]) > 29):
                        return False
                    else:
                        return True
                else:
                    if (int(tanggal[0]) > 28):
                        return False
                    else:
                        return True
            else:
                if (int(tanggal[0]) > 29):
                    return False
                else:
                    return True
        else:
            if (int(tanggal[0]) > 28):
                return False
            else:
                return True
    else:
        return True
    """
    if (tahun % 4) == 0:
        if (tahun % 100) == 0:
            if (tahun % 400) == 0:
                print "Tahun Kabisat"
            else:
                print "Bukan Tahun Kabisat"
        else:
            print "Tahun Kabisat"
    else:
        print "Bukan Tahun Kabisat"
    """

# MAIN
if __name__ == "__main__":
    app.run(debug=True)
