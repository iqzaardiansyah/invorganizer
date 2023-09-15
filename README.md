# invorganizer

https://invorganizer.adaptable.app/

<details>
   <summary>Tugas 2</summary>

   1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

      - Membuat direktori baru (Contoh: "invorganizer").<br>
      - Inisiasi projek Django baru menggunakan CMD yang dialihkan direktori utamanya ke direktori invorganizer dengan command.<br>
      <pre>
         django-admin startproject invorganizer 
      </pre>
      - Masuk ke direktori yang dibuat oleh command sebelumnya menggunakan CMD dan inisiasi virtual environment dengan command.<br>
      <pre>
         python -m venv env
      </pre>
      - Aktifkan virtual environment menggunakan command.<br>
      <pre>
         env\Scripts\activate.bat
      </pre>
      - Salin file requirements.txt dari tutorial 0 dan jalankan command.<br>
      <pre>
         pip install -r requirements.txt
      </pre>
      - Buat app baru bernama main menggunakan command.<br>
      <pre>
         django-admin startapp main
      </pre>
      - Buka settings.py di dalam direktori invorganizer kemudian tambahkan 'main' dalam list INSTALLED_APPS.<br>
      - Buat direktori dalam direktori main bernama "templates" dan buat file bernama "main.html" dan edit sesuai kebutuhan.<br>
      - Edit models.py dalam direktori main dan tambahkan class Item(models.Model) dengan atribut name sebagai nama item dengan tipe CharField, amount sebagai jumlah item dengan tipe IntegerField, description sebagai deskripsi item dengan tipe TextField, dan price sebagai harga item dengan tipe IntegerField.<br>
      - Edit views.py agar menampilkan nama aplikasi, nama mahasiswa, dan kelas sesuai dengan tutorial 1.<br>
      - Buat file bernama "urls.py" dalam direktori main dan isi dengan kode.<br>
      <pre>from django.urls import path
      from main.views import show_main
      app_name = 'main'
      urlpatterns = [
         path('', show_main, name='show_main'),
      ] </pre>
      - Buat Repo baru di github dan salin link HTTPS Repo tersebut.<br>
      - Inisiasi git folder pada direktori project menggunakan CMD dengan command.<br>
      <pre>
         git init
      </pre>
      - Kemudian hubungkan direktori project dengan Repo yang telah dubuat dengan command.<br>
      <pre>
         git remote add origin {link Repo}
      </pre>
      - Push direktori project ke Repo dengan menggunakan mantra git yaitu add, commit, dan push.<br>
      - Buka website adaptable, sign in, dan buat app baru bernama invorganizer dengan mengikuti langkah-langkah pada tutorial 0.<br>
   
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
</details>

<details>
   <summary>Tugas 3</summary>

   1. Apa perbedaan antara form POST dan form GET dalam Django?<br>
   Keduanya digunakan untuk transfer data dari klien ke server melalui protokol HTTP tetapi perbedaan utama antara POST dan GET adalah GET mentransfer parameter *request* dengan format URL *string* sedangkan POST mentransfer paramereter *request* dalam *message body* yang membuat transfer data dari klien ke server menjadi lebih aman.

   2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?<br>
      Perbedaan utama dari ketiga format ini adalah XML dan JSON digunakan untuk menyimpan dan mentransmisikan data sedangkan HTML digunakan untuk menampilkan data. Perbedaan utama antar XML dan JSON adalah kalau JSON merupakan turunan dari JavaScript sedangkan XML turunan dari SGML.

   3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?<br>
      - Dalam kebanyakan kasus, JSON sangat mudah untuk dibaca dibandingkan XML.
      - JSON mempunyai ukuran berkas yang lebih kecil yang menyebabkan pengiriman data menggunkan JSON lebih cepat dibandingkan XML.

   4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).<br>
      - Inisiasi staticfiles di settings.py pada direktori invorganizer dengan langkah-langkah yang telah diajarkan pada tutorial 2.
      - Buat direktori baru bernama templates pada folder root dan buat file base.html.
      - Tambahkan kode berikut ke main.html dan block content & endblock content. Hal ini dilakukan agar main.html menggunakan template utama sebagai kerangka utamanya.
      <pre>
         {% extends 'base.html' %}
      </pre>
      - Buat file baru bernama "forms.py" dalam direktori main dan isi file tersebut dengan kode.
      <pre>
         from django.forms import ModelForm
         from .models import Item
         class ItemForm(ModelForm):
            class Meta:
               model = Item
               fields = ["name", "amount", "price", "description"]
      </pre>
      - Gunakan fungsi show_main untuk menampilkan objek dalam format HTML.
      - Tambahkan fungsi show_xml, show_json, show_xml_by_id, dan show_json_by_id yang menerima parameter request.
      - Tambahkan juga fungsi create_product untuk menambahkan objek tanpa harus mengakses halaman admin.
      - Buat file baru bernama create_product.html dalam folder templates pada direktori main dan isinya sama dengan create_product.html pada tutorial 2.
      - Tambahkan fungsi yang baru dibuat ke urlpatterns dalam file urls.py dalam direktori main dengan menambahkan elemen berikut kedalam list.
      <pre>
         path('create-product', create_product, name='create_product'),
         path('xml/', show_xml, name='show_xml'), 
         path('json/', show_xml, name='show_json'), 
         path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
         path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
      </pre>
      - Akses menggunakan Postman
      ![HTML](image/Screenshot%20(18).png)
      ![XML](image/Screenshot%20(19).png)
      ![JSON](image/Screenshot%20(20).png)
      ![XML by Id](image/Screenshot%20(21).png)
      ![JSON by Id](image/Screenshot%20(22).png)

</details>