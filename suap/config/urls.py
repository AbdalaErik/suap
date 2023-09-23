"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('area/', area, name = 'area'),
    path('avaliacao/', avaliacao, name = 'avaliacao'),
    path('cidade/', cidade, name = 'cidade'),
    path('curso/', curso, name = 'curso'),
    path('disciplina_por_curso/', disciplina_por_curso, name = 'disciplina_por_curso'),
    path('disciplina/', disciplina, name = 'disciplina'),
    path('frequencia/', frequencia, name = 'frequencia'),
    path('instituicao/', instituicao, name = 'instituicao'),
    path('matricula/', matricula, name = 'matricula'),
    path('ocorrencia/', ocorrencia, name = 'ocorrencia'),
    path('ocupacao/', ocupacao, name = 'cupacao'),
    path('periodo/', periodo, name = 'periodo'),
    path('pessoa/', pessoa, name = 'pessoa'),
    path('tipo_de_avaliacao/', tipo_de_avaliacao, name = 'tipo_de_avaliacao'),
    path('turma/', turma, name = 'turma'),
    
]
