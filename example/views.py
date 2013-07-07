from models import Page
from django.shortcuts import render, get_object_or_404

from quiz.models import Quiz
from quiz.forms import CreateQuizForm

def quiz(request):
    
    return render(request, 'page.html', locals())