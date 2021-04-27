import os
from flask import *
import sqlite3 as sql
from KMP import *
from Regex import *
from database import *
from datetime import *

app = Flask(__name__)

# APP_ROUTE = os.path.dirname(os.path.abspath(__file__))

command = [
    'tambah', 'Tambah', # Menambah task baru (poin 1) 
    'update', 'Update', 'ubah', 'Ubah', 'diundur', 'Diundur', 'dimajukan', 'Dimajukan', # Update task (poin 4)
    'deadline', 'Deadline', # Melihat deadline (poin 2/3)
    'selesai', 'Selesai', 'menyelesaikan', 'Menyelesaikan', # Selesai mengerjakan task (poin 5)
    'help', 'Help', 'lakukan', 'Lakukan', 'perintah', 'Perintah', # Menampilkan help (poin 6)
    'paansi'
]

chat = []
nchat = 0

@app.route("/", methods = ['POST', 'GET'])
def index():
    connection = connect() # ini database
    #chat = ["Selamat datang di jam-bot (red: jamboard), masukkan perintah anda"] # array buat nampung chat (string)
    if (len(chat) == 0):
        chat.append("Selamat datang di jam-bot (red: jamboard), masukkan perintah anda")
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
                    addTask(connection, tanggal[0][0], convertBulanToInt(tanggal[0][1]), tanggal[0][2], matkul, jenis, topik)
                    arr = getTaskAll(connection)
                    line = ""
                    #(ID: 1) 14/04/2021 - IF2211 - Tubes - String matching
                    # d, m, y, matkul, jenis, deskripsi
                    for el in arr:
                        line += "(ID: " + str(el[0]) + ") " + str(el[1]) + " - " + str(el[2]) + " - " + str(el[3]) + " - " + str(el[4]) + "<br>"
                    chat.append("[Task Berhasil Dicatat]<br>" + line)
                else:
                    chat.append("Tanggal tidak valid")
            else:
                error = ""
                if (matkul == None):
                    error += "Tidak ada kode matkul<br>"
                if (topik == None):
                    error += "Tidak ada topik tugas<br>"
                if (tanggal == None):
                    error += "Tidak ada tanggal tugas<br>"
                if (jenis == None):
                    error += "Tidak ada jenis tugas<br>"   

                chat.append(error)    
        
        elif (cmd == 'deadline' or cmd == 'Deadline'):
            matkul = searchKodeMatkul(query)
            print(matkul)
            topik = searchTopik(query)
            print(topik)
            tanggal = searchTanggal(query)
            print(tanggal)
            tanggalRelatif = searchTanggalRelatif(query)
            print(tanggalRelatif)
            jenis = searchJenis(query)
            print(jenis)
            # semua kasus
            if (matkul == None and topik == None and tanggal == [] and tanggalRelatif == (None,None) and jenis == None):
                temp = getTaskAll(connection)
                line = ""
                    #(ID: 1) 14/04/2021 - IF2211 - Tubes - String matching
                    # d, m, y, matkul, jenis, deskripsi
                for el in temp:
                    line += "(ID: " + str(el[0]) + ") " + str(el[1]) + " - " + str(el[2]) + " - " + str(el[3]) + " - " + str(el[4]) + "<br>"
                chat.append("[Daftar Deadline]<br>" + line)
                
            # based on tanggal atau period time
            elif ((matkul == None and topik == None and jenis == None) and (tanggal != [] or tanggalRelatif != (None,None))):
                # based on period (1 minggu, 2 hari, 3 bulan, etc)
                satuan = tanggalRelatif[1]
                durasi = int(tanggalRelatif[0])
                if (tanggal==[]):
                    if (satuan == "minggu"):
                        durasi *= 7
                    elif (satuan == "bulan"):
                        durasi *= 30
                    tglAkhir = datetime.now()#.timedelta(days=durasi)
                    tglAkhir = tglAkhir + timedelta(days=durasi)
                    temp = getTaskByPeriod(connection, datetime.now().day, datetime.now().month , datetime.now().year, tglAkhir.day, tglAkhir.month , tglAkhir.year)
                    line = ""
                    for el in temp:
                        line += "(ID: " + str(el[0]) + ") " + str(el[1]) + " - " + str(el[2]) + " - " + str(el[3]) + " - " + str(el[4]) + "<br>"
                    chat.append("[Daftar Deadline]<br>" + line)
                # based on tanggal
                elif(tanggalRelatif==(None,None)):
                    # based on range 2 tanggal 
                    if (len(tanggal)==2):
                        temp = getTaskByPeriod(connection, tanggal[0][0], convertBulanToInt(tanggal[0][1]), tanggal[0][2], tanggal[1][0], convertBulanToInt(tanggal[1][1]), tanggal[1][2])
                        line = ""
                        for el in temp:
                            line += "(ID: " + str(el[0]) + ") " + str(el[1]) + " - " + str(el[2]) + " - " + str(el[3]) + " - " + str(el[4]) + "<br>"
                        chat.append("[Daftar Deadline]<br>" + line)
                    #based on 1 tanggal
                    elif (len(tanggal)==1):
                        temp = getTaskByExactDate(connection, tanggal[0][0], convertBulanToInt(tanggal[0][1]), tanggal[0][2])
                        line = ""
                        for el in temp:
                            line += "(ID: " + str(el[0]) + ") " + str(el[1]) + " - " + str(el[2]) + " - " + str(el[3]) + " - " + str(el[4]) + "<br>"
                        chat.append("[Daftar Deadline]<br>" + line)
            # based on matkul atau jenis kata penting
            elif (topik == None and tanggal == [] and tanggalRelatif == (None,None)) and (matkul != None or jenis!= None):
                if (matkul==None):
                    temp = getTaskByType(connection,jenis)
                    line = ""
                    for el in temp:
                        line += "(ID: " + str(el[0]) + ") " + str(el[1]) + " - " + str(el[2]) + " - " + str(el[3]) + " - " + str(el[4]) + "<br>"
                    chat.append("[Daftar Deadline]<br>" + line)
                elif(jenis==None):
                    temp = getTaskByMatkul(connection,matkul)
                    line = ""
                    for el in temp:
                        line += "(ID: " + str(el[0]) + ") " + str(el[1]) + " - " + str(el[2]) + " - " + str(el[3]) + " - " + str(el[4]) + "<br>"
                    chat.append("[Daftar Deadline]<br>" + line)
                else:
                    temp = getTaskByMatkulType(connection,matkul,jenis)
                    line = ""
                    for el in temp:
                        line += "(ID: " + str(el[0]) + ") " + str(el[1]) + " - " + str(el[2]) + " - " + str(el[3]) + " - " + str(el[4]) + "<br>"
                    chat.append("[Daftar Deadline]<br>" + line)
                       

        elif (cmd == 'update' or cmd == 'Update' or cmd == 'ubah' or cmd == 'Ubah' or cmd == 'diundur' or cmd == 'Diundur' or cmd == 'dimajukan' or cmd == 'Dimajukan'):
            id = searchID(query)
            tanggal = searchTanggal(query)
            if (id != None and tanggal != [] and int(id) > 0 and int(id) <= getMaxId(connection) and isTanggalValid(tanggal[0])):
                updateTaskDeadline(connection, id, tanggal[0][0], tanggal[0][1], tanggal[0][2])
                chat.append("Deadline task " + id + " berhasil diperbarui.")
            else:
                error = ""
                if (id == None):
                    error += "Tidak ada ID task<br>"
                elif (int(id) <= 0 or int(id) > getMaxId()):
                    error += "Task tersebut tidak ditemukan di daftar task<br>"
                if (tanggal == []):
                    error += "Tidak ada tanggal<br>"
                elif (not isTanggalValid(tanggal[0])):
                    error += "Tanggal tidak valid"
                chat.append(error)
        
        elif (cmd == 'selesai' or cmd == 'Selesai' or cmd == 'menyelesaikan' or cmd == 'Menyelesaikan'):
            id = searchID(query)
            if (id != None and int(id) > 0 and int(id) <= getMaxId(connection)):
                deleteTask(connection, id)
                chat.append("Berhasil mengurangi kekeosan")
            else:
                if (id == None):
                    chat.append("Tidak ada ID task")
                elif (int(id) <= 0 or int(id) > getMaxId(connection)):
                    chat.append("Task tersebut tidak ditemukan di daftar task")

        elif (cmd == 'help' or cmd == 'Help' or cmd == 'lakukan' or cmd == 'Lakukan' or cmd == 'perintah' or cmd == 'Perintah'):
            chat.append('''[Fitur]
            <br>1. Menambahkan task baru 
            <br>2. Melihat daftar task 
            <br>3. Menampilkan deadline task
            <br>4. Update task
            <br>5. Menandai task yang sudah selesai
            <br>
            <br>[Daftar kata penting]
            <br>1. Kuis
            <br>2. Ujian
            <br>3. Tucil
            <br>4. Tubes
            <br>5. Mummu
            ''')
                             
        else:
            chat.append("Ngomong apa lo")
        
        print(cmd)
        print(chat)
        #chat.append(cmd)
        

    return render_template("home.html", chat=chat, nchat=len(chat))


def convertBulanToInt(bulan):
    if (bulan == '01' or bulan == "Januari" or bulan == "januari"):
        return '01'
    elif (bulan == '02' or bulan == "Februari" or bulan == "februari"):
        return '02'
    elif (bulan == '03' or bulan == "Maret" or bulan == "maret"):
        return '03'
    elif (bulan == '04' or bulan == "April" or bulan == "april"):
        return '04'
    elif (bulan == '05' or bulan == "Mei" or bulan == "mei"):
        return '05'
    elif (bulan == '06' or bulan == "Juni" or bulan == "juni"):
        return '06'
    elif (bulan == '07' or bulan == "Juli" or bulan == "juli"):
        return '07'
    elif (bulan == '08' or bulan == "Agustus" or bulan == "agustus"):
        return '08'
    elif (bulan == '09' or bulan == "September" or bulan == "september"):
        return '09'
    elif (bulan == '10' or bulan == "Oktober" or bulan == "oktober"):
        return '10'
    elif (bulan == '11' or bulan == "November" or bulan == "november"):
        return '11'
    elif (bulan == '12' or bulan == "Desember" or bulan == "desember"):
        return '12'

def isTanggalValid(tanggal):
    if (tanggal[1] == '4' or tanggal[1] == 'April' or tanggal[1] == 'april'
    or tanggal[1] == '6' or tanggal[1] == 'Juni' or tanggal[1] == 'juni'
    or tanggal[1] == '9' or tanggal[1] == 'September' or tanggal[1] == 'september'
    or tanggal[1] == '11' or tanggal[1] == 'November' or tanggal[1] == 'november'):
        if (tanggal[0] == '31'):
            return False
        else:
            return True
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
