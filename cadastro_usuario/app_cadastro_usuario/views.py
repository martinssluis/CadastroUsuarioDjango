from django.shortcuts import render
from .models import Usuarios


def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    # salvar no BD
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.dt_nasc = request.POST.get('dt_nasc')
    novo_usuario.save()
    #exibir usuarios
    usuarios = {
        'usuarios': Usuarios.objects.all()
    }
    #retornar dados 
    return render(request, 'usuarios/usuarios.html', usuarios)
