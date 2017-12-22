from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {'latest_question_list': [1, 2, 3, 4]}
    return render(request, 'views/index.html', context)


def ficha(request):
    return render(request, 'views/ficha.html')