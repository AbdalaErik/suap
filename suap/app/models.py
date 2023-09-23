from django.db import models

# Create your models here.

class Ocupacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Instituicao(models.Model):
    nome = models.CharField(max_length=50)
    site = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nome} {self.site} {self.telefone}'
    
class Area(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Periodo(models.Model):
    situacao = models.CharField(max_length=20)

    def __str__(self):
        return self.situacao
    
class Turma(models.Model):
    nome = models.CharField(max_length=50)
    periodo = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nome} {self.periodo}'
    
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.nome} {self.uf}'
    
class Tipo_De_Avaliacao(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    pai = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    data_nasc = models.DateField()
    email = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome} {self.pai} {self.mae} {self.cpf} {self.data_nasc} {self.email} {self.cidade}'
    
class Curso(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria_total = models.PositiveIntegerField()
    duracao_meses = models.PositiveIntegerField()
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.carga_horaria_total} {self.duracao_meses} {self.area_saber} {self.instituicao}'
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.area_saber}'
    
class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_prevista_termino = models.DateField()

    def __str__(self):
        return f'{self.instituicao} {self.curso} {self.pessoa} {self.data_inicio} {self.data_prevista_termino}'

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=150)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descricao} {self.curso} {self.disciplina}'
    
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    numero_faltas = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.curso} {self.disciplina} {self.numero_faltas}'

class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=150)
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descricao} {self.data} {self.curso} {self.disciplina} {self.pessoa}'


class Disciplina_Por_Curso(models.Model):
    nome = models.CharField(max_length=50)
    carga_horaria = models.PositiveIntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} {self.carga_horaria} {self.curso} {self.periodo}'