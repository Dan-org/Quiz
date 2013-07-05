from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.template.loader import render_to_string
from django.template import RequestContext, Context, Template, loader
from django.template.loader import add_to_builtins

from models import Quiz, Attempt, Answer
from forms import CreateQuizForm

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User as User
from django.contrib.auth.models import AnonymousUser as AnonymousUser
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.forms.models import model_to_dict
from django.utils import simplejson

#from forms import AjaxForm


# # so that discourse wil work
# add_to_builtins('quiz.templatetags.quiz')

# def quizzes(request):
# 	quizzes = Quiz.objects.all()
# 	return render(request, 'quiz/quizzes.html', locals())

# def quiz(request, quiz_id):
#     """
#     Create a attempt on the quiz.
#     """
#     quiz = get_object_or_404(Quiz, pk=quiz_id) 

#     form = CreateQuizForm(request, quiz=quiz, user=request.user)

#     if form.is_valid():
#         attempt = form.save(quiz)        
#         #notify(critique.author, report, "feedback", critique=critique, report=report)
#         return redirect("quiz_attempt", quiz.id)        
#     #return render(request, "loft/reports/feedback.html", locals())
#     return render(request, "quiz/hello_quiz.html", locals())



def ajax_submit_answer(request):
    quiz_id         = request.GET['quiz_id']
    question_key    = request.GET['question_key']
    answer_key      = request.GET['answer_key']

    quiz        = get_object_or_404(Quiz, pk=quiz_id)
    feedback    = quiz.get_feedback(question_key, answer_key)

    results = { 'success' : True,
                'feedback' : feedback,
                }

    if request.user.is_authenticated():     # if user is logged in...
        attempt, created    = Attempt.objects.get_or_create(user=request.user, quiz=quiz)           # get or create attempt
        answer, created     = Answer.objects.get_or_create(attempt=attempt, question=question_key)  # get or create answer
        answer.answer = answer_key
        attempt.save()
        answer.save()
        #print "saved!"

    return HttpResponse( simplejson.dumps( results ), mimetype='application/json' )

