from django.contrib import admin
from .models import Autenticavel, Usuario
# Register your models here.

class ListandoAutenticaveis(admin.ModelAdmin):
    list_display = ('nome',)
    list_display_links = ('nome',)
    search_field = ('nome',)


class ListandoUsuarios(admin.ModelAdmin):
    list_display = ('login',)
    list_display_links = ('login',)
    search_field = ('login',)


admin.site.register(Usuario, ListandoUsuarios)
admin.site.register(Autenticavel, ListandoAutenticaveis)