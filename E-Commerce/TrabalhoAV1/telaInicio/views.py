from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gameHome(request):
    return render(request, "home.html")


games = [
    {"id": 1, "Title": "jogo 1", "genre": "action"},
    {"id": 2, "Title": "jogo 2", "genre": "rpg"},
    {"id": 3, "Title": "jogo 3", "genre": "strategy"},
]


def listar_Jogo(request):
    context = {"games": games}
    return render(request, "listar_jogo.html", context)


def detalhe_Jogo(request, id):
    game = games[id - 1]
    return render(request, "detalhe_jogo.html", {"game": game})
