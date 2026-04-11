"""
URL configuration for agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views # Aula 02-EX
from django.views.generic import RedirectView # Aula 03: Importando RedirectView para redirecionar para a página de agenda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventos/<str:titulo_evento>/', views.detalhes_evento),
    path('agenda/', views.lista_eventos),
    path('agenda/lista/<int:id_usuario>/', views.json_lista_eventos), # Aula 05: Rota para retornar a lista de eventos em formato JSON
    path('agenda/historico/', views.historico_eventos), # Aula 05-EX: Rota para a página de histórico de eventos
    path('agenda/evento/', views.evento), # Aula 04: Rota para a página de cadastro de eventos
    path('agenda/evento/submit', views.submit_evento), # Aula 04: Rota para processar o cadastro de eventos
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento), # Aula 05: Rota para excluir um evento
    # path('', views.index), # Aula 03: Rota para a página inicial do site
    path('', RedirectView.as_view(url='/agenda/')), # Aula 03: Redirecionando para a página de agenda
    path('login/', views.login_user),
    path('login/submit', views.submit_login), # Aula 04: Rota para processar o login do usuário
    path('logout/', views.logout_user), # Aula 04: Rota para processar o logout do usuário
]
