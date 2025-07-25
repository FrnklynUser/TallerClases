# Generated by Django 5.2.1 on 2025-05-10 22:38

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='DispositivoMovil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imei', models.CharField(max_length=20, unique=True, verbose_name='IMEI')),
                ('numero_celular', models.CharField(max_length=15, verbose_name='Número de celular')),
                ('marca', models.CharField(blank=True, max_length=50, null=True)),
                ('modelo', models.CharField(blank=True, max_length=50, null=True)),
                ('sistema_operativo', models.CharField(blank=True, max_length=50, null=True)),
                ('version_so', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Dispositivo Móvil',
                'verbose_name_plural': 'Dispositivos Móviles',
                'db_table': 'dispositivos',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('perfil_id', models.IntegerField(primary_key=True, serialize=False)),
                ('perfil_nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'perfiles',
            },
        ),
        migrations.CreateModel(
            name='UbicacionDispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitud', models.DecimalField(decimal_places=6, max_digits=9)),
                ('precision', models.FloatField(blank=True, help_text='Precisión en metros', null=True)),
                ('altitud', models.FloatField(blank=True, null=True)),
                ('velocidad', models.FloatField(blank=True, help_text='Velocidad en m/s', null=True)),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ubicaciones', to='accounts.dispositivomovil')),
            ],
            options={
                'verbose_name': 'Ubicación de Dispositivo',
                'verbose_name_plural': 'Ubicaciones de Dispositivos',
                'db_table': 'ubicacion_dispositivos',
                'ordering': ['-fecha_hora'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='usuario_set', related_query_name='usuario', to='auth.group', verbose_name='groups')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='perfiles_usuarios', to='accounts.perfil')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='usuario_set', related_query_name='usuario', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
