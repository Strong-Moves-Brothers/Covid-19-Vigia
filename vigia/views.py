from django.shortcuts import render
import psycopg2
from .models import Usuario
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
        conn = psycopg2.connect(user="postgres",
                                    password="postgrespasswd",
                                    host="vigiadb",
                                    port="5432",
                                    database="vigia")
        
        cursor = conn.cursor()       
        postgreSQL_select_Query = f"select * from autentica where key = '{entry_key}';"
        cursor.execute(postgreSQL_select_Query)
        resultado = cursor.fetchall()
        autenticado = bool(resultado)
        cursor.close()
        conn.close()
        if autenticado:
            return render(request, 'vigia.html')
    except:
        pass
    return render(request, 'autenticacao.html')
