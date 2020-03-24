from django.shortcuts import render
import psycopg2
from .models import Usuario, Autenticavel
# Create your views here.

def index(request):
    return render(request, 'index.html')

def autenticacao(request):
    return render(request, 'autenticacao.html')

def vigia(request):
    return render(request, 'vigia.html')

def autenticar(request):
    entry_key = request.POST['entry_key']
    print(entry_key)
    try:
        autenticado = Autenticavel.objects.get(key=entry_key)
        if autenticado:
            return render(request, 'vigia.html')
    except:
        pass
    return render(request, 'autenticacao.html')
