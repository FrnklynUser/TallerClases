from django.contrib import admin
from .models import *

# Register your models here.
from .models import GrupoArticulo, LineaArticulo

admin.site.register(GrupoArticulo)
admin.site.register(LineaArticulo)