# Generated by Django 3.0.6 on 2020-05-16 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Encuesta')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Survey', verbose_name='Encuesta'),
        ),
    ]
