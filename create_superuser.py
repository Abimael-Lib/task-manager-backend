import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

username = "admin"
password = "TuContraseñaSegura123"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email="", password=password)
    print("Superusuario creado.")
else:
    print("Superusuario ya existe.")
