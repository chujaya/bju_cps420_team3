from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from .models import Question
from django.template import loader
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'check/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'check/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'check/results.html'

def main(request):
    template = loader.get_template('check/main.html')
    context = {
        "template": template
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('check/home.html')
    context = {
        "template": template
    }
    return HttpResponse(template.render(context, request))


def index(request):
    template = loader.get_template('check/index.html')
    context = {
        "template": template
    }
    return HttpResponse(template.render(context, request))