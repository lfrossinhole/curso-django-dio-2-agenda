from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from core.models import Evento # Aula 02-EX
from django.contrib.auth.decorators import login_required # Aula 04: Importando o decorator login_required para proteger as views de eventos
from django.contrib.auth import authenticate, login, logout # Aula 04: Importando as funções authenticate, login e logout para processar o login e logout do usuário
from django.contrib import messages # Aula 04: Importando o módulo messages para exibir mensagens de erro ou sucesso para o usuário

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
                        f'<p>Local do Evento: {evento.local}</p>'
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

# Aula 04: Protegendo a view de eventos para que apenas usuários logados possam acessá-la
def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request) # Aula 04: Realizando o logout do usuário
    return redirect('/') # Aula 04: Redirecionando para a página inicial do site após o logout


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password) # Aula 04: Autenticando o usuário com as credenciais fornecidas
        
        if usuario is not None: # Aula 04: Verificando se o usuário foi autenticado com sucesso
            login(request, usuario) # Aula 04: Realizando o login do usuário
            return redirect('/') # Aula 04: Redirecionando para a página inicial do site após o login bem-sucedido
        else:
            messages.error(request, 'Usuário ou senha inválidos. Tente novamente.') # Aula 04: ele envia uma lista de mensagens de erro para a página de login caso as credenciais sejam inválidas

    return redirect('/login/')

@login_required(login_url='/login/') # Aula 04: quando ele não encontrar o usuário logado, ele vai redirecionar para a página de login
def lista_eventos(request): # Aula 03: Obtendo todos os eventos do banco de dados
    # lista_eventos = Evento.objects.all() # Aula 03: .all retorna uma lista de objetos do tipo Evento
    usuario = request.user # Aula 03: Obtendo o usuário logado
    lista_eventos = Evento.objects.filter(usuario=usuario) # Aula 03: .filter retorna uma lista de objetos do tipo Evento filtrados pelo usuário logado
    dados = {'eventos': lista_eventos}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/') # Aula 04: Protegendo a view de cadastro de eventos para que apenas usuários logados possam acessá-la
def evento(request): # Aula 04: Criando a view para a página de cadastro de eventos
    id_evento = request.GET.get('id') # Aula 05: Obtendo o ID do evento a ser editado a partir dos parâmetros da URL
    dados = {}
    if id_evento: # Aula 05: Verificando se o ID do evento foi fornecido
        dados['evento'] = Evento.objects.get(id=id_evento) # Aula 05: Obtendo o evento a ser editado e adicionando aos dados para exibir na página de cadastro de eventos
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/') # Aula 04: Protegendo a view de processamento de cadastro de eventos para que apenas usuários logados possam acessá-la
def submit_evento(request): # Aula 04: Criando a view para processar o cadastro de eventos
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_evento = request.POST.get('data_evento')
        local = request.POST.get('local')
        usuario = request.user # Aula 04: Obtendo o usuário logado para associar o evento a ele
        id_evento = request.POST.get('id_evento') # Aula 05: Obtendo o ID do evento a ser editado a partir dos dados do formulário

        if id_evento: # Aula 05: Verificando se o ID do evento foi fornecido para edição
            
            # Método 1 EDIÇÃO: Obtendo o evento a ser editado, alterando seus campos e salvando as alterações
            # evento = Evento.objects.get(id=id_evento) # Aula 05: Obtendo o evento a ser editado
            # if evento.usuario == usuario: # Aula 05: Verificando se o usuário logado é o dono do evento a ser editado
            #     evento.titulo = titulo
            #     evento.descricao = descricao
            #     evento.data_evento = data_evento
            #     evento.local = local
            #     evento.save() # Aula 05: Salvando as alterações do evento no banco de dados usando o método save do objeto evento

            # Método 2 EDIÇÃO:
            Evento.objects.filter(id=id_evento).update(titulo=titulo,
                                                        descricao=descricao,
                                                        data_evento=data_evento,
                                                        local=local) # Aula 05: Editando o evento no banco de dados usando o método filter e update, sem precisar obter o objeto evento primeiro

        # Método 1 CRIAÇÃO: Criando o evento e salvando em duas etapas
        # evento = Evento(titulo=titulo, descricao=descricao, data_evento=data_evento, usuario=usuario)
        # evento.save() # Aula 04: Salvando o evento no banco de dados

        # Método 2 CRIAÇÃO:  Aula 04: Criando o evento e salvando em uma única etapa
        else:
            Evento.objects.create(titulo=titulo, 
                                descricao=descricao, 
                                data_evento=data_evento, 
                                local=local, 
                                usuario=usuario)

    return redirect('/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento): # Aula 05: Criando a view para excluir um evento
    usuario = request.user # Aula 05: Obtendo o usuário logado para verificar se ele é o dono do evento
    evento = Evento.objects.get(id=id_evento) # Aula 05: Obtendo o evento pelo ID
    if usuario == evento.usuario: # Aula 05: Verificando se o usuário logado é o dono do evento
        evento.delete() # Aula 05: Excluindo o evento do banco de dados usando o método delete do objeto evento
    
    # Não usou esse método, porque ele não verifica se o usuário logado é o dono do evento, e pode excluir eventos de outros usuários
    # Evento.objects.filter(id=id_evento).delete() # Aula 05: Excluindo o evento do banco de dados usando o método filter e delete
    return redirect('/')