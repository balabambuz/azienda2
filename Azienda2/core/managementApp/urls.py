from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

app_name="managementApp"

urlpatterns = [
    path('', views.lista_dipendenti, name='lista_dipendenti'),
    path('azienda/<slug:azienda_slug>', views.dipendente_azienda, name='dipendente_azienda'),
    path('sede/<slug:sede_slug>', views.dipendente_sede, name='dipendente_sede'),
    path('dipendente/<str:dipendente_nome>', views.dipendente_detail, name='dipendente_detail'),
    #CRUD
    path('crea_dipedente/', views.create_dipendente, name='create_dipendente'),
    path('update_dipendente/<str:nome>', views.update_dipendente, name='update_dipendente'),
    path('delete_dipendente/<str:pk>', views.delete_dipendente, name='delete_dipendente'),
    #Registration
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html',  form_class=AuthenticationForm, next_page='/'), name='login'),

    #path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),


  
   
]