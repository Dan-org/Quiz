from django.conf.urls import patterns, include, url


from django.views.generic import RedirectView

### Urls
urlpatterns = patterns('',
	url(r'^quiz/ajax/submitanswer/$',		'quiz.views.ajax_submit_answer' ),
)
