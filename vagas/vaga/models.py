from django.db import models

area_choices = (
    ('frontend', 'Front-end'),
    ('backend', 'Back-end'),
    ('devops', 'Dev-ops'),
    ('mobile', 'Mobile'),
    ('outro', 'Outro'),
)


class Vaga(models.Model):
    nome = models.CharField(max_length=60, verbose_name='Nome')
    empresa = models.CharField(max_length=60, verbose_name='Empresa')
    descricao = models.TextField(verbose_name='Descrição')
    salario = models.FloatField(verbose_name='Salário')
    area = models.CharField(max_length=60, choices=area_choices, verbose_name='Área')
    linguagem = models.CharField(max_length=60, verbose_name='Linguagem')
    framework = models.CharField(max_length=60, verbose_name='Framework')
    disponivel = models.BooleanField(default=False, verbose_name='Disponível')
    disponivel_ate = models.DateTimeField(verbose_name='Disponível Até')
    contato = models.CharField(max_length=60, verbose_name='Contato')
    disparado = models.BooleanField(default=False, editable=False, verbose_name='Disparado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    uploaded_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

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
