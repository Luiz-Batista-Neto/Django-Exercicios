from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpRequest

usuarios = [
    {"id": 1, "nome": "Travis", "idade": 27},
    {"id": 2, "nome": "Jeane", "idade": 20},
    {"id": 3, "nome": "Lucas", "idade": 37}
]

def listar_Usuarios(request):
    context = {
        "usuarios": usuarios
    }
    return render(request, 'listar_usuarios.html', context)

def detalhes_Usuarios(request, id):
    usuario = usuarios[id - 1]
    return render(request, 'detalhe_usuarios.html', {"usuario": usuario})