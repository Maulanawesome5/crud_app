# Documentation v.0.0.1

## Author : @uzumakiaji

### Cara untuk manajemen container Django Server + DBMS

Ketikkan perintah seperti di bawah ini : 
    1. Membuat django project baru
       * docker-compose run --rm apps django-admin startproject nama_project
    2. Membuat django apps baru
       * docker-compose run --rm apps python manage.py startapp nama_apps
    3. Membuat admin super user
       * docker-compose run --rm apps python manage.py createsuperuser
    4. Migrasi data ke DBMS
       * docker-compose run --rm apps python manage.py migrate
    5. Membuat file migrasi ulang baru
       * docker-compose run --rm apps python manage.py makemigrations

### Menjalankan container Django Server + DBMS bersama

Ketikkan perintah docker-compose up
