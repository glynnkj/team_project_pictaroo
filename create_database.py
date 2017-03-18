import os

print("Delete database")
os.system("rm -rf db.sqlite3")
print("Delete images")
os.system("rm -rf media/images/")
print("Create database")
os.system("python manage.py makemigrations")
os.system("python manage.py migrate --run-syncdb")
print("Populate")
os.system("python populate_pictaroo.py")
print("Create superuser")
os.system("python manage.py createsuperuser")