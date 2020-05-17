from django.contrib import admin
from .models import Question, QuestionChoice, Survey


# Register your models here.

class SurveyAdminRegister(admin.ModelAdmin):
    fieldset = [
        ('Encuesta', {'fields': ['name','active']})
    ]
    list_display = ['name','active','total_preguntas']


admin.site.register(Survey,SurveyAdminRegister)
admin.site.register(Question)
admin.site.register(QuestionChoice)
