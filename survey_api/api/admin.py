from django.contrib import admin

from .models import Survey, Question, UserAnswer

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(UserAnswer)
