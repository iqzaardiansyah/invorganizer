# invorganizer

https://invorganizer.adaptable.app/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   Agar dependensi pengembangan proyek bisa terjaga. Salah satu contoh penggunaan virtual environment adalah pengembangan aplikasi berbasis Django. Salah satu keuntungan menggunakan virtual environment dalam pengembangan aplikasi berbasis Django adalah setiap pengembangan bisa menggunakan versi Python yang berbeda-beda tanpa adanya konflik dari versi Python dari virtual environment yang lain.
5. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   - MVC (Model-View-Controller) : Pola desain yang digunakan untuk mengimplementasikan antarmuka pengguna dan memberikan penekanan pada pemisahan representasi data dari komponen yang berinteraksi dan memproses data.
   - MVT (Model-View-Template) : Pola desain yang mirip dengan MVC, yang jadi pembeda adalah MVT menggunakan Framework untuk menggantika perkerjaan Controller pada MVC.
   - MVVM (Model-View-ViewModel) : Pola desain berbasis GUI yang berfokus pada pemisahan kode untuk logika dan tampilan aplikasi.
   Perbedaan utama antara ketiganya adalah bagaimana mereka mengatur komunikasi antara Model dan View serta pengelolaan logika aplikasi. MVC menggunakan Controller, MVT menggunakan Template, dan MVVM menggunakan ViewModel.
