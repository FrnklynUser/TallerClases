from django.core.management.base import BaseCommand
from accounts.models import Perfil

class Command(BaseCommand):
    help = 'Creates the default admin profile'

    def handle(self, *args, **kwargs):
        try:
            admin_profile, created = Perfil.objects.get_or_create(
                perfil_id=1,
                defaults={'perfil_nombre': 'Administrador'}
            )
            if created:
                self.stdout.write(self.style.SUCCESS('Successfully created admin profile'))
            else:
                self.stdout.write(self.style.SUCCESS('Admin profile already exists'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating admin profile: {str(e)}')) 