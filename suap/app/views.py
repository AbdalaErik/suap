from django.shortcuts import render
from . models import*

# Create your views here.

def pessoa(request):
    consultas = {
        'consultas':Pessoa.objects.all()
    }

    return render(request, 'consulta/pessoa.html', consultas)

def ocupacao(request):
    consultas = {
        'consultas':Ocupacao.objects.all()
    }

    return render(request, 'consulta/ocupacao.html', consultas)

def instituicao(request):
    consultas = {
        'consultas':Instituicao.objects.all()
    }

    return render(request, 'consulta/instituicao.html', consultas)

def area(request):
    consultas = {
        'consultas':Area.objects.all()
    }

    return render(request, 'consulta/area.html', consultas)

def curso(request):
    consultas = {
        'consultas':Curso.objects.all()
    }

    return render(request, 'consulta/curso.html', consultas)

def periodo(request):
    consultas = {
        'consultas':Periodo.objects.all()
    }

    return render(request, 'consulta/periodo.html', consultas)

def disciplina(request):
    consultas = {
        'consultas':Disciplina.objects.all()
    }

    return render(request, 'consulta/disciplina.html', consultas)

def matricula(request):
    consultas = {
        'consultas':Matricula.objects.all()
    }

    return render(request, 'consulta/matricula.html', consultas)

def avaliacao(request):
    consultas = {
        'consultas':Avaliacao.objects.all()
    }

    return render(request, 'consulta/avaliacao.html', consultas)

def disciplina(request):
    consultas = {
        'consultas':Disciplina.objects.all()
    }

    return render(request, 'consulta/disciplina.html', consultas)

def frequencia(request):
    consultas = {
        'consultas':Frequencia.objects.all()
    }

    return render(request, 'consulta/frequencia.html', consultas)

def turma(request):
    consultas = {
        'consultas':Turma.objects.all()
    }

    return render(request, 'consulta/turma.html', consultas)

def cidade(request):
    consultas = {
        'consultas':Cidade.objects.all()
    }

    return render(request, 'consulta/cidade.html', consultas)

def ocorrencia(request):
    consultas = {
        'consultas':Ocorrencia.objects.all()
    }

    return render(request, 'consulta/ocorrencia.html', consultas)

def disciplina_por_curso(request):
    consultas = {
        'consultas':Disciplina_Por_Curso.objects.all()
    }

    return render(request, 'consulta/disciplina_por_curso.html', consultas)

def tipo_de_avaliacao(request):
    consultas = {
        'consultas':Tipo_De_Avaliacao.objects.all()
    }

    return render(request, 'consulta/tipo_de_avaliacao.html', consultas)