from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from core.models import Evento # Aula 02-EX

# Create your views here.

# Alternativa com Try-Except
def detalhes_evento(request, titulo_evento): # Aula 02-EX
    try:
        evento = Evento.objects.get(titulo=titulo_evento)

    except Evento.DoesNotExist:
        return HttpResponse('<h1>Evento não encontrado</h1>', status=404)

    return HttpResponse(f'<h1>Evento: {evento.titulo}</h1>'
                        f'<p>Descrição: {evento.descricao}</p>'
                        f'<p>Data do Evento: {evento.data_evento}</p>'
                        f'<p>Data de Criação: {evento.data_criacao}</p>'
                        f'<p>Usuário: {evento.usuario.username}</p>'
                        )

# # Alternativa com Erro 404
# def detalhes_evento(request, titulo_evento): # Aula 02-EX
#     # Aula 02-EX: Usando get_object_or_404 para buscar o evento pelo título
#     evento = get_object_or_404(Evento, titulo=titulo_evento)
    
#     return HttpResponse(f'<h1>Evento: {evento.titulo}</h1>'
#                         f'<p>Descrição: {evento.descricao}</p>'
#                         f'<p>Data do Evento: {evento.data_evento}</p>'
#                         f'<p>Data de Criação: {evento.data_criacao}</p>'
#                         f'<p>Usuário: {evento.usuario.username}</p>'
#                         )

# Alternativa para redirecionar para a página de agenda
# def index(request): # Aula 03: Criando a view para a página inicial do site
#     return redirect('/agenda/') # Aula 03: Redirecionando para a página de agenda

def lista_eventos(request): # Aula 03: Obtendo todos os eventos do banco de dados
    usuario = request.user # Aula 03: Obtendo o usuário logado
    lista_eventos = Evento.objects.all() # Aula 03: .all retorna uma lista de objetos do tipo Evento
    # lista_eventos = Evento.objects.filter(usuario=usuario) # Aula 03: .filter retorna uma lista de objetos do tipo Evento filtrados pelo usuário logado
    dados = {'eventos': lista_eventos}
    return render(request, 'agenda.html', dados)