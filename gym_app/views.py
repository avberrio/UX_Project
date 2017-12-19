from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def base(request):
    context = {'latest_question_list': [1, 2, 3, 4]}
    return render(request, 'base.html', context)