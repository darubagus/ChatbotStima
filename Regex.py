import re

def searchKodeMatkul(stringCommand):
    # Pencarian kode matkul dengan format IFxxxx dari parameter input
    # Parameter :
        # stringCommand : string
    kodeMatkul = "[Ii][Ff][1234][12][12345][01234]"
    km = re.search(kodeMatkul, stringCommand)
    if (km != None):
        return km.group(0)
    return None

def searchTanggal(stringCommand):
    # Pencarian tanggal dengan format (dd/mm/yyyy) atau (dd-mm-yyyy) atau (dd "nama bulan" yyyy) dari parameter input
    # Parameter :
        # stringCommand : string
    tanggal = "(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012]|[Jj]anuari|[Ff]ebruari|[Mm]aret|[Aa]pril|[Mm]ei|[Jj]uni|[Aa]gustus|[Ss]eptember|[Oo]ktober|[Nn]ovember|[Dd]esember)[- /.](20[0123456789][0123456789])"
    tgl = re.findall(tanggal,stringCommand)
    if (tgl != None):
        return tgl
    return None
    
def searchTopik(stringCommand):
    # Pencarian topik tugas yang terletak di antara kode matkul dan kata "para" dari parameter input
    # Parameter :
        # stringCommand : string
    matkul = searchKodeMatkul(stringCommand)
    if (matkul == None):
        return None
    pattern = "(?<=" + matkul +" )(.*)"+"(?=pada)"
    topik = re.search(pattern, stringCommand)
    if (topik != None):
        return topik.group(0)
    return None

def searchJenis(stringCommand):
    # Pencarian jenis tugas yang terletak di dalam parameter input, tidak peduli dimanapun letaknya
    # Parameter :
        # stringCommand : string
    jenisTugas = "[Tt](ubes|ucil)|[Kk]uis|[Uu]jian|[Pp]raktikum|[Mm]ummu"
    jenis = re.search(jenisTugas, stringCommand)
    if (jenis != None):
        return jenis.group(0)
    return None

def searchTanggalRelatif(stringCommand):
    # Pencarian tanggal dengan format (x hari/minggu/bulan) dari parameter input
    # Parameter :
        # stringCommand : string
    satuan = "(?<= )"+"(hari|minggu|bulan)"
    tglRelatif = re.search(satuan, stringCommand)
    angka = "(?<=)([123456789][0123456789]*)"+"(?= (hari|minggu|bulan))"
    searchAngka = re.search(angka, stringCommand)
    if (tglRelatif != None and searchAngka != None):
        return searchAngka.group(0), tglRelatif.group(0)
    return None, None

def searchIDorTask(stringCommand):
    # Pencarian keyword id/ID/Id/Task/task dari parameter input, tidak peduli dimanapun letaknya
    # Parameter :
        # stringCommand : string
    idOrTask = re.search("(id|Id|ID|[Tt]ask)", stringCommand)
    if idOrTask != None:
        return idOrTask.group(0)
    return None

def searchID(stringCommand):
    # Pencarian id task setelah kata id/ID/Id/Task(id/ID/Id/Task/task) dari parameter input
    # Parameter :
        # stringCommand : string
    idOrTask = searchIDorTask(stringCommand)
    if (idOrTask == None):
        return None
    id = "(?<="+idOrTask+" )([123456789][0123456789]*)"
    taskid = re.search(id, stringCommand)
    if (taskid != None):
        return taskid.group(0)
    return None
    