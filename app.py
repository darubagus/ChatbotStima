import os
from flask import *
import sqlite3 as sql
from KMP import *

app = Flask(__name__)

# APP_ROUTE = os.path.dirname(os.path.abspath(__file__))

kataPenting = [
    'tucil' , 'Tucil' ,
    'tubes', 'Tubes' ,
    'kuis', 'Kuis' ,
    'ujian', 'Ujian' ,
    'praktikum', 'Praktikum' ,
    'mummu' , 'Mummu'
]

command = [
    'tambah', 'Tambah', # Menambah task baru (poin 1) 
    'deadline', 'Deadline', # Melihat deadline (poin 2/3)
    'daftar', 'Daftar', 'list', 'List ',  # Melihat daftar tugas (poin 2)
    'update', 'Update', 'ubah', 'Ubah', 'diundur', 'Diundur', 'dimajukan', 'Dimajukan', # Update task (poin 4)
    'selesai', 'Selesai', # Selesai mengerjakan task (poin 5)
    'help', 'Help', 'lakukan', 'Lakukan', 'perintah', 'Perintah' # Menampilkan help (poin 6)
]

@app.route("/")
def index():
    query = request.args.get('query') # variabel query di html
    
    return render_template("home.html")




# MAIN
if __name__ == "__main__":
    app.run(debug=True)