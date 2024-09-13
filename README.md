# 08-indonesia-complete-blog-app
Membuat A COMPLETE BLOG APP Menggunakan Django 5
Github: https://github.com/gurnitha/08-indonesia-complete-blog-app


## 1. SETUP

#### 1. Lokasi proyek 

#### 2. Membuat remote repositori di Github 

#### 3. Mengklon repositori dari Github

#### 4. Git commit 

#### 5. Restrukturisasi file proyek dan membuat root direktori

        modified:   README.md

#### 6. Mendorong file proyek ke remote repositori di Github

#### 7. Membuat lingkungan virtual 

#### 8. Aktivasi dan deaktivasi lingkungan virtual

#### 9. Menginstal Django 

#### 10. Meng-upgrade pip 

#### 11. Contoh teknik pembuatan proyek Django


## 2. PROYEK DJANGO

#### 1. Memeriksa sub-perintah yang tersedia pada django-admin

        C:\Users\ING\Desktop\workspace\08-indonesia-complete-blog-app\src(main -> origin)
        (venv312511) λ django-admin

        Type 'django-admin help <subcommand>' for help on a specific subcommand.

        Available subcommands:

        [django]
            check
            compilemessages
            createcachetable
            dbshell
            diffsettings
            dumpdata
            flush
            inspectdb
            loaddata
            makemessages
            makemigrations
            migrate
            optimizemigration
            runserver
            sendtestemail
            shell
            showmigrations
            sqlflush
            sqlmigrate
            sqlsequencereset
            squashmigrations
            startapp
            startproject
            test
            testserver
        Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).

#### 2. Menginisiasi Django proyek dengan nama config

        (venv312511) λ django-admin startproject config .
        
        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

        src
        ├── README.md
        ├── config
        │   ├── __init__.py
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── manage.py