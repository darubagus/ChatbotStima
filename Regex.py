import re

# month = "[Jj]anuari|[Ff]ebruari|[Mm]aret|[Aa]pril|[Mm]ei|[Jj]uni|[Aa]gustus|[Ss]eptember|[Oo]ktober|[Nn]ovember|[Dd]esember"
kodeMatkul = "(IF|if)[1234][12][12345][01234]"
tanggal = "(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012]|[Jj]anuari|[Ff]ebruari|[Mm]aret|[Aa]pril|[Mm]ei|[Jj]uni|[Aa]gustus|[Ss]eptember|[Oo]ktober|[Nn]ovember|[Dd]esember)[- /.](20[0123456789][0123456789])"
jenisTugas = "[Tt](ubes|ucil)|[Kk]uis|[Uu]jian|[Pp]raktikum|[Mm]ummu"

def searchKodeMatkul(stringCommand):
    km = re.search(kodeMatkul, stringCommand)
    if (km != None):
        return km.group(0)
    return None

def searchTanggal(stringCommand):
    # tanggal itu setelah kata "pada" atau setelah "antara"
    # tanggal = re.search("(?<=pada )(.*)[0-9]", stringTanggal) or re.search("(?<=antara )(.*)[0-9]", stringTanggal)
    tgl = re.findall(tanggal,stringCommand)
    if (tgl != None):
        return tgl
    return None
    
def searchTopik(stringCommand):
    matkul = searchKodeMatkul(stringCommand)
    pattern = "(?<=" + matkul +" )(.*)"+"(?=pada)"
    topik = re.search(pattern, stringCommand)
    if (topik != None):
        return topik.group(0)
    return None

def searchJenis(stringCommand):
    jenis = re.search(jenisTugas, stringCommand)
    if (jenis != None):
        return jenis.group(0)
    return None
#DEBUGpy
print(searchKodeMatkul("menambahkan matkul IF2211"))
print(searchTanggal("antara 13 Januari 2021"))

# format <command> <jenis tugas> <matkul> <topik> pada <tanggal>
command = "coba tambah kuis IF2211 Review Liburan Pa Rila pada 14 April 2021"
print(searchJenis(command))
print(searchTopik(command))