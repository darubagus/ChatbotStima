# Jam-Bot
## Penunjang Produktivitas
Tugas Besar IF2211 Strategi Algoritma<br>
Program Studi Teknik Informatika<br>
Institut Teknologi Bandung<br>
2021

## Description
Jam-Bot adalah sebuah aplikasi chatbot berbasis web. Sesuai dengan taglinenya, Jam-Bot dapat membantu penggunanya untuk menunjang tingkat produktivitasnya dengan cara menyediakan layanan berupa task reminder milik pengguna. Jam-Bot dapat menyimpan kode mata kuliah, tenggat waktu tugas, jenis tugas, dan deskripsi tugas yang diberikan oleh pengguna. Untuk memahami pesan yang diberikan, Jam-Bot memanfaatkan Algoritma String Matching versi Knuth-Morris Pratt dan Algoritma Regular Expression.

## Algoritma KMP dan Regex
KMP merupakan singkatan dari Knuth-Morris Pratt, yang tak lain adalah penemu dari algoritma tersebut. Algoritma KMP berfungsi sebagai algoritma string matching, yaitu pencarian sebuah pattern dari string yang diberikan. Sebuah pattern didefinisikan ada dalam sebuah string jika setiap karakter dalam pattern tersebut berada dalam sebuah string dengan keterurutan yang sama. Pada proses pencocokan, Algoritma KMP akan menyimpan prefix dari maksimum n karakter pada pattern yang sama dengan string yang merupakan suffix dari n-1 karakter terakhir pattern tersebut. Algoritma KMP akan menggeser pattern sejauh posisi pertama karakter berbeda dikurangi panjang prefix/suffix yang dicari sebelumnya sehingga proses pencarian pattern dapat dilakukan dengan lebih efektif. Algoritma KMP memiliki kompleksitas waktu O(m+n), dimana m adalah panjang pattern dan n adalah panjang string. Penjelasan lebih lengkap dari Algoritma KMP dapat dilihat di [sini.](https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2020-2021/Pencocokan-string-2021.pdf)

Sementara itu, Regex merupakan singkatan dari Regular Expression. Sama seperti KMP, Regex juga merupakan algoritma yang dapat mencari sebuah pattern dari sebuah string tertentu. Regex memanfaatkan sintaks yang dapat menerima beragam kemungkinan pattern yang ingin kita cari dalam string. Dengan menggunakan Regex, pattern yang diberikan bisa lebih dari satu macam, bahkan tak berhingga jumlahnya dengan pola yang didefinisikan. Penjelasan lebih lengkap dari Algoritma Regex dapat dilihat di [sini.](https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2018-2019/String-Matching-dengan-Regex-2019.pdf)

## Requirements
Sebelum memulai program pastikan anda sudah memiliki pip pada python. Instruksi untuk instalasi pip dapat dilihat di [sini](https://www.geeksforgeeks.org/download-and-install-pip-latest-version/)

Kemudian pastikan anda sudah memiliki library berikut:
* flask
* sastrawi
* nltk

Untuk melakukan instalasi cukup menjalankan perintah pada terminal:

* `pip install <nama_library>` (untuk sistem operasi Windows dan Linux)
* `pip3 install <nama_library>` (untuk sistem operasi MacOS)

Khusus untuk library nltk, silahkan menjalankan python pada terminal, lalu tuliskan:

`import nltk `

`nltk.download()`

Instruksi lebih lengkap bisa dilihat di [sini](https://www.guru99.com/download-install-nltk.html)

## How to use
Untuk menjalankan Jam-Bot, ikuti langkah-langkah berikut:
* Jalankan `app.py` pada terminal anda.
* Anda akan diarahkan ke localhost `http://127.0.0.1:5000/` di browser anda.
* Masuk ke laman localhost tersebut
* Tuliskan perintah yang ingin anda lakukan

## Keyword List
* Menambah task baru: `tambah`, `ingetin`, `ingat`. 
* Melihat deadline task: `deadline`, `kumpul`, `tenggat`, `ngumpulin`.
* Mengubah deadline task: `update`, `ubah`, `undur`, `maju`, `baharu`, `baru`
* Menyelesaikan task: `selesai`, `kelar`, `beres`, `rampung`.
* Menampilkan bantuan: `help`, `laku`, `perintah`, `bantu`. <br>
Note: Keyword tetap bisa berfungsi untuk perintah berimbuhan dalam Bahasa Indonesia yang baik dan benar.

## Author
Program ini dibuat oleh:
* Daru Bagus Dananjaya - 13519080
* Ryo Richardo - 13519193
* Rayhan Asadel - 13519196
