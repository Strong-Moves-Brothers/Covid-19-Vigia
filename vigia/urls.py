from django.urls import path
from . import views

urlpatterns = [
                path('', views.index, name='index'),
                path('vigia', views.vigia, name='vigia'),
                path('autenticacao', views.autenticacao, name='autenticacao'),
                path('autenticar', views.autenticar, name='autenticar')
                ]