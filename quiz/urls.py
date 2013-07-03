from django.conf.urls import patterns, include, url


from django.views.generic import RedirectView

### Urls
urlpatterns = patterns('',

    url(r'^quizzes/$',                      'quiz.views.quizzes',   name="all_quizzes"),
    url(r'^quiz/(?P<quiz_id>[\w-]+)/$',     'quiz.views.quiz',      name="quiz"),

	url(r'^quiz/ajax/submitanswer/$',		'quiz.views.ajax_submit_answer' ),
)
