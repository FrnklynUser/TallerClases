import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'post_project.settings')
django.setup()

from accounts.models import Perfil

# Create admin profile if it doesn't exist
try:
    admin_profile = Perfil.objects.get_or_create(
        perfil_id=1,
        perfil_nombre='Administrador'
    )
    print('Perfil de Administrador creado exitosamente')
except Exception as e:
    print(f'Error al crear el perfil: {str(e)}') 