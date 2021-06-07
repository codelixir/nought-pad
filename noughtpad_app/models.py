from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    'Model for a note/post in the blog'
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + " | " + str(self.author)

    # def __init__(self):
    #     ...
