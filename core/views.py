from django.shortcuts import render, HttpResponse
from .models import Evento # Aula 02-EX


# Create your views here.

def detalhes_evento(request, titulo_evento): # Aula 02-EX
    evento = Evento.objects.get(titulo=titulo_evento)
    
    return HttpResponse(f'<h1>Evento: {evento.titulo}</h1>'
                        f'<p>Descrição: {evento.descricao}</p>'
                        f'<p>Data do Evento: {evento.data_evento}</p>'
                        f'<p>Data de Criação: {evento.data_criacao}</p>'
                        f'<p>Usuário: {evento.usuario.username}</p>'
                        )