import datetime
from django.db import models

# Create your models here.
from django.utils import timezone


class Survey(models.Model):
    name = models.CharField(
        verbose_name='Encuesta',
        max_length=250
    )

    active = models.BooleanField(
        verbose_name='Activo',
        default=True,
    )

    @property
    def total_preguntas(self):
        return len(Question.objects.filter(survey_id=self.pk))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuestas'





class Question(models.Model):
    survey_id = models.ForeignKey(
        to=Survey,
        on_delete=models.CASCADE,
        verbose_name='Encuesta',
        null=True
    )

    question = models.CharField(
        verbose_name='Pregunta',
        max_length=250,
    )
    publish_date = models.DateTimeField(
        verbose_name='Fecha de publicación'
    )

    def __str__(self):
        return self.question

    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'


class QuestionChoice(models.Model):
    question_id = models.ForeignKey(
        to=Question,
        on_delete=models.CASCADE,
        verbose_name='Pregunta',
    )
    choice = models.CharField(
        verbose_name='Opción',
        max_length=250,
    )
    votes = models.IntegerField(
        default=0,
        verbose_name='Total de votos',
    )

    def __str__(self):
        return self.choice

    class Meta:
        verbose_name = 'Opción'
        verbose_name_plural = 'Opciones'
