from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^$', 								'quizsite.views.quiz'),       
    url(r'', include('quiz.urls')),
)
