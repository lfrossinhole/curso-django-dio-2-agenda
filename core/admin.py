from django.contrib import admin
from core.models import Evento # Aula 02

# Register your models here.

class EventoAdmin(admin.ModelAdmin): # Aula 02
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento',)

admin.site.register(Evento, EventoAdmin) # Aula 02