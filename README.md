link aplikasi PWS: https://marlond-leanderd-soco-footballshop.pbp.cs.ui.ac.id/
Nama aplikasi: SoCo (Soccer Commerce)

Tugas 2
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


Tugas 3: Implementasi Form dan Data Delivery pada Django
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Jawaban: Data delivery adalah cara untuk mengirim dan menampilkan data dari server ke pengguna atau ke sistem lain. Tanpa data delivery, aplikasi tidak dapat menampilkan informasi yang dibutuhkan oleh user. Sebagai contoh, toko online perlu mengirim data produk dari database ke halaman web agar pembeli bisa melihat daftar barang.

    
2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Jawaban: JSON lebih sering dipakai karena lebih ringkas dan tidak banyak tag seperti XML, mudah dipahami oleh manusia dan juga komputer, serta lebih cocok digunakan untuk aplikasi modern, sehingga JSON dapat dikatakan lebih praktis dan membuatnya lebih populer dibandingkan XML.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Jawaban: is_valid() merupakan fungsi yang berguna untuk mengecek apakah data yang diisi oleh pengguna sudah benar. Jika semua data sudah sesuai atau valid, maka data baru bisa disimpan ke database. Jika tidak valid. Django akan memberi tahu error-nya. Method ini diperlukan agar data yang masuk ke database sudah dipastikan aman dan sesuai dengan aturan yang diterapkan.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    Jawaban: csrf_token difungsikan sebagai pengaman agar form hanya dapat dikirimkan dari website kita sendiri. Jika tidak ada csrf_token, pihak luar dapat membuat form palsu di luar website dan memaksa pengguna yang sedang login untuk mengirim data tanpa sadar, seperti ketika pengguna ingin memesan barang atau mengganti data penting. Dengan menggunakan csrf_token, serangan seperti ini tidak dapat dilakukan.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Jawaban: 
        a. Langkah pertama yang dilakukan adalah membuat base template terlebih dahulu. Base template diletakkan dalam file base.html sebagai kerangka utama proyek.
        b. Langkah selanjutnya adalah dengan melakukan finalisasi model product terlebih dahulu dengan menambahkan field seperti product_views dan created_at. Saya juga menambahkan beberapa kategori yang bisa dipilih sesuai dengan produk yang ingin dijual. Disini saya perlu menjalankan kembali python manage.py makemigrations dan python manage.py migrate karena mengubah model yang ada.
        c. Dilanjutkan dengan membuat form yaitu membuat ProductForm dengan field yang dapat diisi oleh pemilik toko.
        d. Berikutnya adalah menambahkan beberapa fungsi dalam views.py, seperti create_product, show_product, serta endpoint untuk show_json, show_xml, show_json_by_id, show_xml_by_id.
        e. Fungsi-fungsi yang telah ditambahkan di views.py kemudian dihubungkan ke urls.py dengan membuat URL routing, misalnya /json/, /xml/, /json/<id>/, /xml/<id>/.
        f. Langkah berikutnya adalah membuat template halaman seperti form tambah produk (create_product.html) dan detail produk (product_detail.html) serta menampilkan daftar produk menggunakan main.html.
        g. Setelah itu, proyek dicoba untuk dijalankan secara lokal melalui komputer, menambahkan produk baru lewat form, serta mencoba membuka endpoint JSON dan XML untuk melihat data produk yang telah ditambah melalui form.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    Jawaban: Tutorial yang disediakan oleh asisten dosen telah menjelaskan bagian form dan data delivery dengan rinci sehingga dapat membantu memahami dasar penggunaan template, form, dan data delivery di Django. 

berikut terlampir hasil screenshot ketika mengakses 4 URL di poin 2 menggunakan Postman:
![alt text](<JSON on Postman.png>)
![alt text](<XML on Postman.png>)
![alt text](<JSON with ID on Postman.png>)
![alt text](<XML with ID on Postman.png>)

Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    Jawaban: Django AuthenticationForm adalah form bawaan Django untuk proses login dengan username dan password. Form ini sudah menyiapkan validasi, pesan error, dan integrasi langsung dengan sistem autentikasi Django sehingga praktis digunakan. Kelebihannya adalah aman, siap untuk dipakai, dan minim terhadap konfigurasi tambahan. Namun, kekurangan yang dimiliki adalah hanya cocok untuk kebutuhan dasar saja, sehingga untuk login dengan menggunakan metode khusus seperti OTP atau SSO harus tetap perlu kustomisasi.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    Jawaban: Autentikasi adalah proses memverifikasi identitas pengguna, sedangkan otorisasi menentukan hak akses pengguna serta terverifikasi. Di Django, autentikasi dilakukan dengan fungsi authenticate() dan login(), serta middleware yang menempelkan informasi user pada setiap request. Otorisasi dikelola lewat sistem permission dan decorator seperti @login_required. Dengan cara ini Django dapat memisahkan "siapa dirimu" dan secara jelas.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    Jawaban: Session menyimpan data di server, sedangkan cookies bisa menyimpan data langsung di browser. Session lebih aman karena informasi sensitif tidak ada di sisi klien, tetapi membutuhkan penyimpanan dan pengelolaan di server. Cookies lebih ringan dan sederhana, namun rentan dimodifikasi atau dicuri jika tidak diamankan.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    Jawaban: Cookies tidak sepenuhnya aman secara default karena masih ada risiko XSS, CSRF, atau pencurian data jika tidak dikonfigurasi dengan benar. Django membantu melakukan pencegahan dengan fitur bawaan seperti HttpOnly, Secure, dan middleware CSRF. Dengan konfigurasi yang tepat dan penggunaan HTTPS, cookies dalam Django bisa digunakan secara aman.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    Jawaban:
    - Aktifkan virtual environment agar konfigurasi proyek terisolasi dari sistem.
    - Gunakan form bawaan Django yaitu UserCreationForm untuk daftar akun baru. Buat halaman register, validasi password atau username, lalu simpan user. Tampilkan pesan sukses dan arahkan ke login. 
    - Pakai AuthenticationForm untuk validasi login. Jika benar, user masuk dan diarahkan ke halaman utama. Kalau salah, tetap di halaman login dengan pesan error.
    - Tambahkan fungsi logout untuk hapus sesi user. Setelah keluar, arahkan ke login lagi. Tampilkan tombol logout di halaman utama agar mudah diakses.
    - Gunakan decorator login_required di halaman penting. Kalau belum login, otomatis diarahkan ke halaman login. Dengan ini, konten hanya bisa dibuka oleh user terautentikasi.
    - Saat login berhasil, simpan waktu login terakhir ke cookie. Tampilkan di halaman utama agar user tahu aktivitas terakhir. Hapus cookie ketika logout supaya data bersih.
    - Tambahkan relasi user ke model Product. Saat membuat produk, otomatis catat pemiliknya dari user yang login. Filter produk bisa ditampilkan “semua” atau “milik saya”.
    - Tambahkan tombol “All Products” dan “My Products" untuk ganti filter dengan cepat. Tampilkan nama user yang sedang login di halaman utama agar terasa personal.
    - Coba daftar akun, login, buat produk, cek filter, lalu logout. Pastikan setiap alur bekerja sesuai harapan, termasuk cookie last_login muncul dan hilang.

Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    Jawaban:
        Dalam pengembangan web, ketika sebuah elemen HTML ditargetkan oleh beberapa selector CSS, browser menentukan style mana yang akan diterapkan berdasarkan sistem prioritas yang disebut Spesifisitas. Prioritas ini berjalan dari yang paling spesifik ke yang paling umum. Inline styles, yang ditulis langsung di atribut style elemen, memiliki prioritas tertinggi, diikuti oleh ID selectors yang menggunakan #, kemudian class, attribute, dan pseudo-class selector, seperti .nama-kelas, [type="text"], atau :hover. Prioritas terendah diberikan kepada element selectors, yaiu menargetkan nama tag HTML seperti div atau p. Terdapat aturan !important yang dapat mengesampingkan semua prioritas ini, namun penggunaannya sangat tidak disarankan karena mempersulit debugging dan pemeliharaan kode.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
    Jawaban:
        Responsive design adalah konsep krusial dalam pengembangan web modern yang memungkinkan tampilan aplikasi beradaptasi secara mulus di berbagai perangkat, dari desktop hingga mobile. Pentingnya ini terletak pada beberapa aspek. Pertama, hal ini meningkatkan Pengalaman Pengguna (UX) secara signifikan karena sebagian besar pengguna mengakses web melalui mobile, memastikan konten mudah dibaca dan dinavigasi tanpa perlu zoom. Kedua, desain responsif memperluas jangkauan audiens. Terakhir, ini lebih efisien dalam pengembangan karena hanya memerlukan satu basis kode. Sebagai contoh, YouTube sangat responsif. Di desktop ia menampilkan layout grid multi-kolom dengan sidebar, sementara di mobile berubah menjadi feed vertikal satu kolom dengan navigasi di bagian bawah. Sebaliknya, beberapa situs pemerintah atau akademis yang lebih tua seringkali tidak responsif, menampilkan layout desktop yang menyusut di mobile, memaksa pengguna untuk melakukan pinch-and-zoom yang sangat tidak praktis.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
    Jawaban:
        Margin, border, dan padding adalah tiga komponen utama dari CSS Box Model yang mengatur tata letak dan jarak di sekitar elemen HTML, dapat dianalogikan dengan sebuah bingkai foto. Padding adalah ruang transparan di dalam border yang berfungsi untuk memisahkan konten dari batasnya. Jika elemen memiliki warna latar, padding akan ikut berwarna. Contoh implementasi Tailwind adalah p-4 dan pt-4. Border adalah garis visual yang mengelilingi padding dan konten, menentukan batas elemen. Contoh implementasi Tailwind adalah border, border-gray-200. Terakhir, margin adalah ruang transparan di luar border, berfungsi untuk memberi jarak elemen dari elemen lain. Margin tidak akan ikut berwarna jika elemen diberi latar belakang. Contoh implementasi Tailwind adalah m-4, mb-8, dan mx-auto. 

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
    Jawaban:
        Flexbox dan Grid Layout adalah dua tool fundamental dalam CSS untuk mengatur posisi dan perataan elemen di halaman web. Flexbox dirancang untuk layout satu dimensi, baik sebagai baris atau kolom. Ini ideal untuk menyusun elemen-elemen di dalam sebuah komponen, seperti menyejajarkan logo dan link di dalam navbar, atau mengatur ikon dan teks dalam sebuah tombol. Dalam proyek ini, navbar dan tombol filter diimplementasikan menggunakan Flexbox. Di sisi lain, Grid Layout bekerja dalam dua dimensi (baris dan kolom secara bersamaan), dapat berfungsi sebagai struktur layout halaman secara keseluruhan. Contohnya, Grid digunakan untuk membuat galeri produk dengan jumlah kolom yang adaptif terhadap ukuran layar (grid-cols-1 md:grid-cols-2 lg:grid-cols-3), yang memberikan kontrol penuh atas penempatan item di halaman.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    Jawaban:
        - Saya memulai dengan mengimplementasikan fitur Edit dan Delete untuk produk. Ini melibatkan pembuatan fungsi view edit_product dan delete_product di views.py, mendaftarkannya di urls.py, dan menambahkan tombol pemicunya di halaman utama. Logika otorisasi {% if user == product.user %} ditambahkan untuk memastikan hanya pemilik yang bisa mengakses fitur ini.
        - Saya memilih Tailwind CSS sesuai tutorial dan mengintegrasikannya ke proyek melalui CDN di base.html.
        - Saya membangun Navbar yang responsif. Mengadaptasi contoh tutorial, saya membuat navbar fixed yang menampilkan link di desktop dan berubah menjadi hamburger menu fungsional di mobile. Saya menyesuaikan branding dan link agar sesuai dengan kebutuhan "SoCo". Skrip untuk toggle menu dipindahkan ke base.html untuk fungsionalitas yang lebih stabil di semua halaman.
        - Saya mengubah main.html. Mengikuti pola tutorial, saya membuat komponen terpisah card_product.html untuk setiap item. Kemudian, di main.html, saya menggunakan CSS Grid (grid grid-cols-1, md:grid-cols-2 lg:grid-cols-3) untuk menyusun kartu-kartu tersebut dalam layout yang rapi dan responsif.
        - Untuk halaman Login, Register, Add Product, dan Edit Product, saya mengadaptasi template dari tutorial. Saya menggunakan layout modern seperti split-screen untuk halaman autentikasi dan card-based form untuk halaman lainnya, serta memastikan semua input field diberi styling yang konsisten dari forms.py.
        - Di halaman utama, saya mengimplementasikan logika {% if not product_list %} untuk menampilkan pesan dan gambar "No products found", sesuai dengan instruksi.
        - Saya menetapkan skema warna ungu di seluruh aplikasi, mulai dari logo "SoCo", tombol, hingga link aktif untuk menciptakan identitas visual yang kuat.
        - Saya menambahkan hero section dengan gambar latar di halaman utama untuk meningkatkan daya tarik visual.
        - Saya melakukan beberapa perbaikan di luar tutorial, seperti mengganti link "Edit/Delete" dengan ikon, menambahkan indikator stok dinamis pada kartu produk, dan memformat harga (Rp 2.000.000) menggunakan django.contrib.humanize agar lebih mudah dibaca.

Tugas 6: Javascript dan AJAX
1. Apa perbedaan antara synchronous request dan asynchronous request?
    Jawaban:
        Perbedaan utama antara request synchronous dan asynchronous terletak pada bagaimana browser menangani alur kerja dan interaksi pengguna. Dalam model sinkron, browser akan mengirim permintaan dan "membeku" (blocking), memaksa pengguna untuk menunggu hingga respons diterima sebelum dapat melakukan hal lain. Sebaliknya, model asinkron memungkinkan browser mengirim permintaan di latar belakang (non-blocking) sementara pengguna tetap bebas berinteraksi dengan halaman. Pendekatan asinkron inilah yang digunakan oleh AJAX untuk menciptakan pengalaman pengguna yang mulus, cepat, dan responsif tanpa ada jeda yang mengganggu.

2. Bagaimana AJAX bekerja di Django (alur request–response)?
    Jawaban:
        AJAX di Django bekerja dengan menciptakan jembatan antara aksi pengguna di browser dan logika di server tanpa me-reload halaman. Alurnya dimulai ketika sebuah event (seperti klik tombol) dicegat oleh JavaScript, yang kemudian membatalkan aksi default browser. JavaScript lalu menggunakan Fetch API untuk mengirim permintaan data ke URL Django yang spesifik. Di sisi server, view Django yang sesuai akan memproses permintaan ini, berinteraksi dengan database, dan mengembalikan data dalam format JSON menggunakan JsonResponse, bukan merender seluruh halaman HTML. Akhirnya, JavaScript di browser menerima data JSON ini dan secara dinamis memanipulasi DOM untuk memperbarui tampilan—seperti menambahkan produk baru atau menampilkan pesan sehingga perubahan terjadi secara instan di halaman yang sama.

3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
    Jawaban:
        Keuntungan utama menggunakan AJAX dibandingkan render biasa di Django adalah peningkatan drastis pada pengalaman pengguna (UX) dan efisiensi. Dengan AJAX, interaksi terasa instan karena halaman tidak perlu dimuat ulang seluruhnya, menghilangkan kedipan layar yang mengganggu dan membuat website terasa secepat aplikasi desktop. Selain itu, AJAX jauh lebih efisien dalam penggunaan bandwidth karena hanya data yang relevan (dalam format JSON yang ringan) yang dipertukarkan antara server dan klien, tidak seperti render biasa yang harus memuat ulang seluruh aset HTML, CSS, dan JavaScript. Hal ini tidak hanya mempercepat waktu muat tetapi juga mengurangi beban kerja pada server secara signifikan.

4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
    Jawaban:
        Untuk memastikan keamanan saat menggunakan AJAX untuk otentikasi, ada beberapa langkah krusial yang harus diterapkan. Pertama dan terpenting adalah menggunakan proteksi CSRF (Cross-Site Request Forgery) bawaan Django dengan cara menyertakan CSRF token di dalam header setiap request AJAX POST. Kedua, seluruh komunikasi wajib dienkripsi menggunakan HTTPS (SSL/TLS) untuk mencegah data sensitif seperti password dicuri dalam perjalanan. Terakhir, semua data yang dikirim dari form harus divalidasi ulang secara ketat di sisi server (views.py) untuk memastikan integritas data dan mencegah injeksi kode berbahaya, sambil tetap menggunakan mekanisme password hashing standar dari Django.

5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
    Jawaban:
        AJAX secara fundamental mengubah pengalaman pengguna dengan membuat website terasa jauh lebih responsif, mulus, dan interaktif. Karena pembaruan konten terjadi di latar belakang tanpa me-reload halaman, pengguna tidak mengalami transisi yang kasar atau jeda yang mengganggu, sehingga menciptakan alur interaksi yang berkelanjutan. Hal ini memberikan persepsi kecepatan yang jauh lebih tinggi, karena pengguna mendapatkan umpan balik visual secara instan (seperti loading spinner atau toast notification) sambil tetap berada di konteks halaman yang sama. Hasilnya adalah pengalaman yang lebih memuaskan dan tidak membuat frustrasi, mirip dengan kelancaran saat menggunakan aplikasi di ponsel atau desktop.

