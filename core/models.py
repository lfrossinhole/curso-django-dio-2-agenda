from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

class Evento(models.Model): # Aula 02
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    local = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # O nome da tabela será "evento" e não "core_evento"
    class Meta:
        db_table = 'evento'

    # O método __str__ é utilizado para exibir o nome do evento no admin do Django
    def __str__(self): # Aula 02
        return self.titulo
    
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y - %H:%M Hrs')
    
    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')
    
    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False
    
    # Modulo 05 - Faz um evento que está vencendo (faltando 1 hora para o evento) ficar amarelo
    def get_evento_vencendo(self):
        if self.data_evento < datetime.now() + timedelta(hours=1):
            return True
        else:
            return False