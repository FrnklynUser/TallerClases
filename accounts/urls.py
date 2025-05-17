from django.urls import path
from .views import profile_view, profile_update, login_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path('perfil/', profile_view, name='profile'), 
    path('perfil/actualizar/', profile_update, name='profile_update'), 
    
    # URLs de autenticación
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]  