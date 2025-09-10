link aplikasi PWS: https://marlond-leanderd-soco-footballshop.pbp.cs.ui.ac.id/
Nama aplikasi: SoCo (Soccer Commerce)

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    a.  Membuat sebuah proyek Django baru.
        jawaban:
        Saya lakukan dengan cara membuat virtual environment terlebih dahulu menggunakan line code berikut pada terminal:
        - python -m venv env
        - source env/bin/activate 

        Lalu saya menginstall Django menggunakan line code berikut pada terminal:
        - pip install django

        Lalu saya membuat proyek Django bernama football_shop menggunakan line code berikut pada terminal:
        - django-admin startproject football_shop .

    b. Membuat aplikasi dengan nama main pada proyek tersebut.
        jawaban:
        Saya lakukan dengan cara menggunakan line code berikut pada terminal:
        - python manage.py startapp main
        Selanjutnya, saya tambahkan 'main' di bagian INSTALLED_APPS yang terdapat pada file settings.py. Hal ini dilakukan agar Django dapat mengetahui bahwa aplikasi 'main' dapat digunakan.

    c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        jawaban:
        Saya lakukan dengan cara membuat perubahan pada file urls.py yang terdapat pada direktori main, lalu sambungkan file urls.py tersebut dengan file urls.py yang terdapat dalam direktori football_shop menggunakan keyword include.

    d. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib.
        jawaban:
        Saya lakukan dengan cara menambahkan model Product pada file models.py dengan beberapa field wajib yang telah diberikan dalam ketentuan tugas, yaitu name (nama produk), price (harga produk), description (deskripsi produk), thumbnail (link gambar produk), category (kategori produk), dan is_featured (produk yang disukai atau bukan).
        Setelah menambahkan model Product pada file models.py, saya melakukan migrasi dengan menjalankan 2 line code berikut pada terminal:
        - python manage.py makemigrations
        - python manage.py migrate
        Hal ini dilakukan tiap kali terdapat perubahan skema pada models.py

    e.  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
        jawaban:
        Saya lakukan dengan cara membuat show_main terlebih dahulu pada views.py yang terdapat pada direktori main yang berisi nama aplikasi, nama diri, npm, dan kelas. Informasi yang terdapat pada views.py kemudian diberikan kepada main.html yang terdapat pada direktori templates yang dapat ditemukan pada direktori main. Semua informasi yang terdapat pada views.py dapat ditampilkan melalui main.html dengan menggunakan key yang sesuai.
        Setelah itu, saya coba cek dengan mengetik "python manage.py runserver" pada terminal, lalu masuk ke http://127.0.0.1:8000/ untuk melihat apakah tampilan yang dikeluarkan sudah sesuai dengan harapan atau belum.

    f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        jawaban:
        Langkah ini sudah dilakukan pada tahap c, yaitu urls.py yang terdapat pada direktori main memetakan '' ke show_main, lalu di-include di urls.py yang terdapat dalam direktori football_shop. 

    g. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        jawaban:
        Langkah pertama yang dilakukan adalah memastikan bahwa AllOWED_HOSTS yang terdapat dalam file settings.py di direktori football_shop telah memuat domain PWS saya, yaitu https://marlond-leanderd-soco-footballshop.pbp.cs.ui.ac.id/. Setelah itu, saya melakukan add dan push ke repositori GitHub, serta mengetikkan line code:
        - git push pws main:master
        Untuk deploy aplikasi yang dibuat ke PWS.

    h. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
        jawaban:
        Saya buat di dalam direktori utama football-shop, lalu menjawab beberapa pertanyaan dan melakukan git add, commit, push untuk dimasukkan ke dalam repositori GitHub. 

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    jawaban: 
    ![alt text](<Bagan tugas individu 2.png>)
    Penjelasan:
    1. Client -> urls.py
        - Client mengirim HTTP request ke server.
        - urls.py akan memeriksa apakah path request cocok dengan pola tertentu.
        - Jika cocok, maka akan diarahkan ke fungsi yang terdapat di views.py. Jika tidak cocok, maka akan menampilkan "404 Not Found".
    
    2. urls.py -> views.py
        - urls.py berfungsi sebagai router.
        - View yang sesuai akan dipanggil untuk menangani request.
    
    3. views.py -> models.py
        - View biasanya akan membutuhkan data dari database.
        - views.py akan memanggil models.py untuk melakukan query.

    4. models.py -> views.py
        - Model mengembalikan objek hasil query ke view.
        - Data ini belum menjadi tampilan melainkan masih dalam bentuk objek Python.

    5. views.py -> Template HTML
        - View memasukkan data ke dalam template HTML menggunakan context dictionary.
        - Template berisi struktur tampilan (HTML) dan placeholder ({{ ... }}).

    6. Template HTML -> Client/Response
        - Template akan dirender dan menghasilkan HTML akhir.
        - HTML akan dikirim kembali ke browser sebagai HTTP Response.
        - Browser akan menampilkan hasil ke user.

3. Jelaskan peran settings.py dalam proyek Django!
    jawaban: settings.py dalam proyek Django secara garis besar berperan sebagai pusat pengaturan. Semua aturan utama proyek yang dibuat bisa didapatkan di settings.py. Sebagai salah satu contoh settings.py sebagai pusat pengaturan dalam proyek yang sedang dikembangkan, terdapat daftar INSTALLED_APPS, yang berisi aplikasi bawaan Django serta aplikasi buatan kita, dalam kasus ini berarti aplikasi main.

4. Bagaimana cara kerja migrasi database di Django?
    jawaban: Kita perlu mendefinisikan model yang diinginkan di models.py yang terdapat pada direktori main terlebih dahulu. Setelah itu, ketikkan perintah "python manage.py makemigrations" pada terminal. Perintah makemigrations akan membuat file migrasi yang menyimpan perubahan skema. Lalu, ketikkan perintah "python manage.py migrate" pada terminal. Perintah migrate akan mengeksekusi migrasi dan menerapkan perubahan yang telah disimpan ke database. Django memiliki sifat yaitu menyimpan aktivitas migrasi sehingga perubahan skema dapat terlacak dan bisa diulang.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    jawaban: Menurut pendapat saya, framework Django cocok untuk dijadikan permulaan pembelajaran pengembangan perangkat lunak karena memudahkan pemula untuk dapat memahami pemisahan keperluan (logika, tampilan, dan data). Walaupun framework Django dapat dioperasikan pemula, namun framework ini mampu untuk mengerjakan proyek besar, sehingga pemula dapat mengeksplor pengembangan perangkat lunak lebih luas.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    jawaban: Tidak ada. Semua langkah-langkah yang diberikan dalam tutorial 1 sudah jelas, dan saya dapat menerapkannya dengan baik ketika melakukan pembelajaran pengembangan perangkat lunak menggunakan framework Django.