# Generated by Django 3.2.6 on 2021-08-18 17:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vaga', '0002_auto_criado_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='contato',
            field=models.CharField(default=django.utils.timezone.now, max_length=60, verbose_name='Contato'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vaga',
            name='disparado',
            field=models.BooleanField(default=False, editable=False, verbose_name='Disparado'),
        ),
    ]