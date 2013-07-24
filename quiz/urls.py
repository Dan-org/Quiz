from django.conf.urls import patterns, include, url


from django.views.generic import RedirectView

### Urls
urlpatterns = patterns('',
	url(r'^ajax/submitanswer/$',  'quiz.views.ajax_submit_answer', name="quiz_ajax_url"),
)
