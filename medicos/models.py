from django.db import models

class Medico(models.Model):
    # Campos da selecao de medicos
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    tempo_consulta = models.IntegerField()
    foto_perfil = models.ImageField(upload_to='fotos_medicos/', default="")

    # Campos da pagina do medico
    foto_fundo = models.ImageField(upload_to='fundos_medicos/', default="")
    crm = models.CharField(max_length=20, default="")
    residencia = models.TextField(default="")
    descricao = models.TextField(default="")
    patologias = models.TextField(default="")
    atendimento = models.TextField(default="")
    convenio = models.TextField(default="")
    retorno = models.TextField(default="")
    experiencia = models.TextField(default="")
    stars = models.FloatField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


class Formacao(models.Model):
    #Modelo para as formacoes
    medico = models.ForeignKey(Medico, related_name="formacoes", on_delete=models.CASCADE)
    faculdade_nome = models.CharField(max_length=255)
    curso_nome = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.faculdade_nome} - {self.curso_nome}"
