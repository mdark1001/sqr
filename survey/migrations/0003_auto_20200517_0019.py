# Generated by Django 3.0.6 on 2020-05-17 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20200516_2327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Pregunta', 'verbose_name_plural': 'Preguntas'},
        ),
        migrations.AlterModelOptions(
            name='questionchoice',
            options={'verbose_name': 'Opción', 'verbose_name_plural': 'Opciones'},
        ),
        migrations.AlterModelOptions(
            name='survey',
            options={'verbose_name': 'Encuesta', 'verbose_name_plural': 'Encuestas'},
        ),
        migrations.AddField(
            model_name='survey',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]