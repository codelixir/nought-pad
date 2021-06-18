from django.contrib import admin
from .models import Note, Category, Comment, Profile

admin.site.register(Note)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Comment)
