from django.urls import path
from app_cadastro_usuario import views


urlpatterns = [
   # rota, view responsavel, nome referencia 
   path('', views.home, name='home'), #default (pagina inicial)
   path('usuarios/', views.usuarios, name='listagem_usuarios')
]
