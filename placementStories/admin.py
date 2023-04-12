from django.contrib import admin
from .models import story, question, answer
# Register your models here.
admin.site.register(story)
admin.site.register(question)
admin.site.register(answer)
