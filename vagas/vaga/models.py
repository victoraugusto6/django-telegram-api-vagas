from django.db import models


class Vaga(models.Model):
    nome = models.CharField(max_length=60)
    empresa = models.CharField(max_length=60)
    descricao = models.TextField()
    salario = models.FloatField()
    area = models.CharField(max_length=60)
    linguagem = models.CharField(max_length=60)
    framework = models.CharField(max_length=60)
    disponivel = models.BooleanField(default=False)
    disponivel_ate = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    def vaga_to_dict(self):
        return {
            "id": self.pk,
            "nome": self.nome,
            "empresa": self.empresa,
            "descricao": self.descricao,
            "salario": self.salario,
            "area": self.area,
            "linguagem": self.linguagem,
            "framework": self.framework,
            "disponivel": self.disponivel,
            "disponivel_ate": self.disponivel_ate,
            "created_at": self.created_at,
            "uploaded_at": self.uploaded_at
        }
