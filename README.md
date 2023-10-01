# invorganizer

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

<details>

   <summary>Tugas 4</summary>

   1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?<br>
   Django memiliki sistem otentikasi pengguna bawaan yang bernama `UserCreationForm` yang berguna untuk membuat pengguna baru yang bisa menggunakan aplikasi yang kita buat. `UserCreationForm` memiliki tiga _fields_ yaitu _username_, _password1_, dan _password2_.

   2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?<br>
   Kalau autentikasi memverikasi bahwa pengguna yang menggunakan adalah pengguna yang seharusnya, sedangkan otorisasi menentukan apa yang bisa dilakukan oleh pengguna yang diautentikasi.

   3. Apa itu _cookies_ dalam konteks aplikasi web, dan bagaimana Django menggunakan _cookies_ untuk mengelola data sesi pengguna?<br>
   _Cookies_ adalah berkas yang berisi informasi yang dikirim oleh web server ke browser. Browser menyimpan _cookie_ yang diterima dalam jangka waktu yang telah ditentukan, atau sampai pengguna _logout_ dari suatu _website_. Cara Django menggunakan _cookies_ untuk mengelola data sesi pengguna adalah dengan menggunakan _cookies_ untuk menyimpan _session id_ sedangkan data sesi aslinya akan tetap disimpan di _database_ karena kalau disimpan di _cookies_, sistem akan rentan terhadap serangan. 

   4. Apakah penggunaan _cookies_ aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?<br>
   _Cookies_ sebenarnya bukan sebuah ancaman tetapi _cookies_ bisa digunakan oleh penjahat siber untuk _masquerading_, mengambil data finansial, mengakses akun pengguna, atau mencuri kata sandi pengguna yang tersimpan di browser.

   5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).<br>
      - Buat file yang diperlukan untuk register, login, dan logout seperti `register.html` dan `login.html`.
      - Isi `register.html` dan `login.html` dengan kode yang diberikan pada tutorial 3.
      - Tambahkan kode berikut ke `views.py` yang ada di direktori `main` agar aplikasi memiliki fitur login, logout, register, _cookies_, menampilkan nama pengguna, menampilkan sesi terakhir login, dan menampilkan Item spesifik untuk setiap pengguna.
      <pre>
      
      ...
      
      from django.shortcuts import redirect
      from django.contrib.auth.forms import UserCreationForm
      from django.contrib import messages
      from django.contrib.auth import authenticate, login
      import datetime
   
      ...
   
      def show_main(request):
         list = Item.objects.all().filter(user=request.user)
   
         context = {
           'name': request.user.username,
           'class': 'PBP F',
           'list' : list,
           'count': count,
           'last_login': request.COOKIES['last_login'],
         }
   
      ...
   
       def create_product(request):
         form = ItemForm(request.POST or None)
   
         if form.is_valid() and request.method == "POST":
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return HttpResponseRedirect(reverse('main:show_main'))
   
      ...
   
      def register(request):
         form = UserCreationForm()
   
         if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  form.save()
                  messages.success(request, 'Your account has been successfully created!')
                  return redirect('main:login')
         context = {'form':form}
         return render(request, 'register.html', context)
   
      ...
   
      def login_user(request):
         if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
               login(request, user)
               response = HttpResponseRedirect(reverse("main:show_main")) 
               response.set_cookie('last_login', str(datetime.datetime.now()))
               return response
            else:
               messages.info(request, 'Sorry, incorrect username or password. Please try again.')
         context = {}
         return render(request, 'login.html', context)
   
      ...
   
      def logout_user(request):
         logout(request)
         response = HttpResponseRedirect(reverse('main:login'))
         response.delete_cookie('last_login')
         return response
   
      </pre>
   
      - Impor fungsi-fungsi yang telah dibuat dan tambahkan _path url_ ke `urlpatterns` untuk mengakses fungsi yang telah dibuat pada file `urls.py` dalam direktori `main`.
   
      - Tambahkan kode berikut ke dalam `views.py` dalam direktori `main`  agar aplikasi yang dibuat hanya bisa digunakan oleh pengguna yang sudah diautentikasi.
      <pre>
      
      from django.contrib.auth.decorators import login_required
   
      ...
   
      @login_required(login_url='/login')
      def show_main(request):
   
      ...
      
      </pre>
   
      - Tambahkan kode berikut ke dalam `models.py` pada direktori `main` agar Item yang ditampilkan spesifik untuk setiap pengguna.
      <pre>
      
      ...
      from django.contrib.auth.models import User
      ...
   
      class Item(models.Model):
         user = models.ForeignKey(User, on_delete=models.CASCADE)
      ...
      
      </pre>
   
      - Aktifkan _virtual environment_ dan lakukan `python manage.py makemigrations` dan `python manage.py migrate`.
</details>

<details>

   <summary>Tugas 5</summary>

   1. Jelaskan manfaat dari setiap _element selector_ dan kapan waktu yang tepat untuk menggunakannya.<br>
   _Element selector_ dalam CSS digunakan untuk mengubah properti semua elemen yang memiliki tag HTML yang sama. Ada beberapa manfaat dalam menggunakan setiap _element selector_, dan waktu yang tepat untuk menggunakannya ketika dalam pengembangan aplikasi dibutuhkan properti yang berbeda-beda berdasarkan tag HTML-nya.

   2. Jelaskan HTML5 Tag yang kamu ketahui.<br>
      * !DOCTYPE : Tag untuk menentukan tipe dokumen.
      * html : Tag untuk membuat sebuah dokumen HTML.
      * title : Tag untuk membuat judul dari sebuah halaman.
      * body : Tag untuk membuat tubuh dari sebuah halaman.
      * h1 to h6 : Tag untuk membuat heading.
      * p : Tag untuk membuat paragraf.
      * br : Memasukan satu baris putus.
      * hr : Tag untuk membuat perubahan dasar kata di dalam isi.
      * !--...-- : Tag untuk membuat komentar.

   3. Jelaskan perbedaan antara _margin_ dan _padding_.<br>
      * _Margin_ : Ruang di luar elemen, yang berarti itu adalah jarak antara elemen tersebut dan elemen-elemen lain di sekitarnya. _Margin_ digunakan untuk mengontrol jarak antara elemen dengan elemen-elemen lain di luar elemen tersebut.
      * _Padding_ : Ruang di dalam elemen, yang berarti itu adalah jarak antara batas elemen dan konten di dalamnya. _Padding_ digunakan untuk mengatur jarak antara konten elemen dan batas elemen itu sendiri.

   4. Jelaskan perbedaan antara _framework_ CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
      * Bootstrap adalah framework CSS yang sudah dirancang dengan gaya yang sudah ditentukan (_pre-designed_). Ini berarti Bootstrap menyediakan komponen dan gaya bawaan yang siap digunakan, sehingga memungkinkan Anda membangun situs web dengan cepat tanpa banyak penyesuaian. Bootstrap sebaiknya digunakan jika diperlukan tampilan yang cepat & mudah tanpa banyak kustomisasi, ingin membangun prototipe dengan cepat, dan tidak memiliki waktu atau kebutuhan untuk membangun desain kustom dari nol.
      * Tailwind menyediakan banyak kelas CSS yang fleksibel, seperti `.bg-blue-500`, `.p-4`, atau `.flex`. Tailwind lebih cocok untuk kustomisasi yang mendalam karena Tailwind dapat membangun desain dari awal dengan menggunakan kelas-kelas utilitas yang ada. Tailwind sebaiknya digunakan jika diinginkan desain yang sangat kustom dan sesuai dengan kebutuhan proyek.
   5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
      * Tambahkan _method `remove`_ yang berguna untuk menghapus objek yang telah dibuat, _method `decrement`_ & _`increment`_ yang berguna untuk mengubah _field amount_ suatu objek, *method `edit_product`* yang berguna untuk mengedit suatu objek, dan *method `BacktoMain`* yang berguna untuk kembali ke halaman utama ketika menekan judul halaman yang terletak di NavBar.<br>
         <pre>
            ...
            def remove(request, id):
               product = Item.objects.get(pk = id)
               product.delete()
               return HttpResponseRedirect(reverse('main:show_main'))
            
            def decrement(request, id = None):
               object = Item.objects.get(pk = id)
               object.amount -= 1
               object.save()
               return HttpResponseRedirect(reverse('main:show_main'))
            
            def increment(request, id = None):
               object = Item.objects.get(pk = id)
               object.amount += 1
               object.save()
               return HttpResponseRedirect(reverse('main:show_main'))
            
            def BacktoMain(request):
               return HttpResponseRedirect(reverse('main:show_main'))
            
            def edit_product(request, id):
               object = Item.objects.get(pk = id)
               form = ItemForm(request.POST or None, instance=object)
               if form.is_valid() and request.method == "POST":
                  form.save()
                  return HttpResponseRedirect(reverse('main:show_main'))
               context = {'form': form}
               return render(request, "edit_product.html", context)
         </pre>
      * Tambahkan *method-method* yang baru dibuat ke `views.py`.
         <pre>
            ...
            from main.views import *
            ...
            urlpatterns = [
               path('', show_main, name='show_main'),
               path('create-product', create_product, name='create_product'),
               path('xml/', show_xml, name='show_xml'), 
               path('json/', show_json, name='show_json'), 
               path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
               path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
               path('register/', register, name='register'),
               path('login/', login_user, name='login'),
               path('logout/', logout_user, name='logout'),
               path('remove/<int:id>', remove, name="remove"),
               path('decrement/<int:id>', decrement, name='decrement'),
               path('edit-product/<int:id>', edit_product, name='edit_product'),
               path('backtomain/', BacktoMain, name='backtomain'),
               path('increment/<int:id>', increment, name='increment'),
            ]
         </pre>
      * Inisiasi Bootstrap CSS dan juga JS dengan menambahkan beberapa kode ke *`base.html`*.
      * Inisiasi NavBar pada *`base.html`* dan buat _block_ baru pada NavBar agar setiap halaman bisa memiliki properti NavBar-nya masing-masing
      * Pindahkan tombol _logout_ ke NavBar.
      * Tambahkan beberapa tombol pada *_main.html_* untuk menggunakan _method-method_ yang baru dibuat.
      * Ubah _table_ yang digunakan sebelumnya menjadi _card_.
      * Kustomisasi _card_ menggunakan tag _style_.

</details>