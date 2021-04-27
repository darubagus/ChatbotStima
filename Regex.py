import re

# month = "[Jj]anuari|[Ff]ebruari|[Mm]aret|[Aa]pril|[Mm]ei|[Jj]uni|[Aa]gustus|[Ss]eptember|[Oo]ktober|[Nn]ovember|[Dd]esember"


def searchKodeMatkul(stringCommand):
    kodeMatkul = "(IF|if)[1234][12][12345][01234]"
    km = re.search(kodeMatkul, stringCommand)
    if (km != None):
        return km.group(0)
    return None

def searchTanggal(stringCommand):
    # tanggal itu setelah kata "pada" atau setelah "antara"
    # tanggal = re.search("(?<=pada )(.*)[0-9]", stringTanggal) or re.search("(?<=antara )(.*)[0-9]", stringTanggal)
    tanggal = "(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012]|[Jj]anuari|[Ff]ebruari|[Mm]aret|[Aa]pril|[Mm]ei|[Jj]uni|[Aa]gustus|[Ss]eptember|[Oo]ktober|[Nn]ovember|[Dd]esember)[- /.](20[0123456789][0123456789])"
    tgl = re.findall(tanggal,stringCommand)
    if (tgl != None):
        return tgl
    return None
    
def searchTopik(stringCommand):
    matkul = searchKodeMatkul(stringCommand)
    if (matkul == None):
        return None
    pattern = "(?<=" + matkul +" )(.*)"+"(?=pada)"
    topik = re.search(pattern, stringCommand)
    if (topik != None):
        return topik.group(0)
    return None

def searchJenis(stringCommand):
    jenisTugas = "[Tt](ubes|ucil)|[Kk]uis|[Uu]jian|[Pp]raktikum|[Mm]ummu"
    jenis = re.search(jenisTugas, stringCommand)
    if (jenis != None):
        return jenis.group(0)
    return None

def searchTanggalRelatif(stringCommand):
    satuan = "(?<= )"+"(hari|minggu|bulan)"
    tglRelatif = re.search(satuan, stringCommand)
    angka = "(?<=)([123456789][0123456789]*)"+"(?= (hari|minggu|bulan))"
    searchAngka = re.search(angka, stringCommand)
    if (tglRelatif != None and searchAngka != None):
        return searchAngka.group(0), tglRelatif.group(0)
    return None, None

def searchIDorTask(stringCommand):
    idOrTask = re.search("(id|Id|ID|[Tt]ask)", stringCommand)
    if idOrTask != None:
        return idOrTask.group(0)
    return None

def searchID(stringCommand):
    idOrTask = searchIDorTask(stringCommand)
    if (idOrTask == None):
        return None
    id = "(?<="+idOrTask+" )([123456789][0123456789]*)"
    taskid = re.search(id, stringCommand)
    if (taskid != None):
        return taskid.group(0)
    return None
    
#DEBUGpy
#print(searchKodeMatkul("menambahkan matkul IF2211"))
print(searchTanggal("antara 13 Januari 2021"))
#
## format <command> <jenis tugas> <matkul> <topik> pada <tanggal>
#command = "tambah"
# commandDeadline = "Antara 03/04/2021 dan 15/04/2021 ada deadline apa saja ya?"
commandUpdateID = "task 1 diundur"
print(searchID(commandUpdateID))
#print(searchJenis(command))
#print(searchTopik(command))
#print(searchTanggalRelatif(commandDeadline))
#print(searchTanggal(commandDeadline)[1][0])
