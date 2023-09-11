# invorganizer

https://invorganizer.adaptable.app/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   - Membuat direktori baru (Contoh: "invorganizer").
   - Inisiasi projek Django baru menggunakan CMD yang dialihkan direktori utamanya ke direktori invorganizer dengan command "django-admin startproject invorganizer".
   - Masuk ke direktori yang dibuat oleh command sebelumnya menggunakan CMD dan inisiasi virtual environment dengan command "py -m venv env".
   - Aktifkan virtual environment menggunakan command "env\Scripts\activate.bat".
   - Salin file requirements.txt dari tutorial 0 dan jalankan command "pip install -r requirements.txt".
   - Jalankan command "django-admin startapp main" untuk membuat app baru bernama main.
   - Buka settings.py di dalam direktori invorganizer kemudian tambahkan 'main' dalam list INSTALLED_APPS.
   - Buat direktori dalam direktori main bernama "templates" dan buat file bernama "main.html".
   - Edit models.py dalam direktori main dan tambahkan class Item(models.Model) dengan atribut name sebagai nama item dengan tipe CharField, amount sebagai jumlah item dengan tipe IntegerField, description sebagai deskripsi item dengan tipe TextField, dan price sebagai harga item dengan tipe IntegerField.
   - Edit views.py agar menampilkan nama aplikasi, nama mahasiswa, dan kelas sesuai dengan tutorial 1.
   - Buat file bernama "urls.py" dalam direktori main dan isi dengan kode.<br>
     <pre>from django.urls import path
     from main.views import show_main
     app_name = 'main'
     urlpatterns = [
        path('', show_main, name='show_main'),
     ] <pre>
   - Buat Repo baru di github dan salin link HTTPS Repo tersebut.
   - Inisiasi git folder pada direktori project menggunakan CMD dengan kode "git init".
   - Kemudian hubungkan direktori project dengan Repo yang telah dubuat dengan command "git remote add origin (link HTTPS)".
   - Push direktori project ke Repo dengan menggunakan mantra git yaitu add, commit, dan push.
   - Buka website adaptable, sign in, dan buat app baru bernama invorganizer dengan mengikuti langkah-langkah pada tutorial 0.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.<br>
![bagan](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page/basic-django.png)<br>
Ketika Django mendeteksi adanya HTTP Request, Django akan mencoba untuk mencocokkan URL yang diminta ke daftar URL yang ada di dalam file urls.py. Setiap URL dipetakan ke fungsi tertentu yang ada di dalam file views.py, sehingga ketika URL yang diminta ditemukan, maka fungsi yang terpetakan ke URL tersebut akan dipanggil. Fungsi yang terpetakan ke URL tersebut kemudian mengambil alih penanganan Request dan mengembalikan respons. Request umumnya memerlukan semacam interaksi dengan database, yang diwakili oleh objek yang ditentukan dalam file models.py. Fungsi yang terpetakan ke URL tersebut akan mengambil objek model dari database, dan menyiapkan respons ke klien. Respon ini kemudian ditampilkan di browser klien menggunakan template yang memiliki format HTML.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?<br>
Agar dependensi pengembangan proyek bisa terjaga. Salah satu contoh penggunaan virtual environment adalah pengembangan aplikasi berbasis Django. Salah satu keuntungan menggunakan virtual environment dalam pengembangan aplikasi berbasis Django adalah setiap pengembangan bisa menggunakan versi Python yang berbeda-beda tanpa adanya konflik dari versi Python dari virtual environment yang lain. 
   
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   - MVC (Model-View-Controller) : Pola desain yang digunakan untuk mengimplementasikan antarmuka pengguna dan memberikan penekanan pada pemisahan representasi data dari komponen yang berinteraksi dan memproses data.
   - MVT (Model-View-Template) : Pola desain yang mirip dengan MVC, yang jadi pembeda adalah MVT menggunakan Framework untuk menggantika perkerjaan Controller pada MVC.
   - MVVM (Model-View-ViewModel) : Pola desain berbasis GUI yang berfokus pada pemisahan kode untuk logika dan tampilan aplikasi.
   Perbedaan utama antara ketiganya adalah bagaimana mereka mengatur komunikasi antara Model dan View serta pengelolaan logika aplikasi. MVC menggunakan Controller, MVT menggunakan Template, dan MVVM menggunakan ViewModel.
