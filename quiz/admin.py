from django.contrib import admin

from models import Quiz, Answer, Attempt


admin.site.register(Quiz)
admin.site.register(Attempt)
admin.site.register(Answer)