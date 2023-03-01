from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest

usuarios = [
    {"Id": 1, "Nome": "Travis", "Idade": 27},
    {"Id": 2, "Nome": "Jeane", "Idade": 20},
    {"Id": 3, "Nome": "Lucas", "Idade": 37}
]

def listar_Usuarios(request):
    context = {
        "Usuarios": usuarios
    }
    return render(request, 'listar_usuarios.html', context)

def detalhes_Usuarios(request):
    usuario = usuarios[id - 1]
    return render(request, 'detalhe_usuarios.html', {"usuario": usuario})