from django.db import models

class Politica(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Analise(models.Model):
    politica = models.OneToOneField(
        Politica,
        on_delete=models.CASCADE,
        related_name='analise'
    )
    resultado = models.TextField()
    analisado_em = models.DateTimeField(auto_now_add=True)