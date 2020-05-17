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


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'survey/detail.html', {'question': question})


def result(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
