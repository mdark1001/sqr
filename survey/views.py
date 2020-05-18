from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question, Survey


# Create your views here.

def index(request):
    surveys = Survey.objects.filter(active=True)
    context = {
        'surveys': surveys,
    }
    return render(request, 'survey/index.html', context)


def detail(request, survey_id):
    try:
        survey = Survey.objects.get(pk=survey_id)
    except Survey.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'survey/detail.html', {'survey': survey})


def edit(request, survey_id):
    try:
        survey = Survey.objects.get(pk=survey_id)
    except Survey.DoesNotExist:
        raise Http404("Survey does not exist")
    return render(request, 'survey/edit.html', {'survey': survey})


def result(request, survey_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % survey_id)


def vote(request, survey_id):
    return HttpResponse("You're voting on question %s." % survey_id)
