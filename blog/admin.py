from django.contrib import admin
from .models import Question,Person,Choice
# Register your models here.
admin.site.register(Question)
admin.site.register(Person)
admin.site.register(Choice)

