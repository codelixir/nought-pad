from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Note(models.Model):
    'Model for a note/post in the blog'
    title = models.CharField(max_length=255)
    banner = models.ImageField(
        null=True, blank=True, upload_to="user_content/images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Miscellaneous')
    likes = models.ManyToManyField(User, related_name='post')

    def __str__(self):
        return self.title + " | " + str(self.author)

    # this method is required to submit the form
    def get_absolute_url(self):
        return reverse("note-details", kwargs={"pk": self.pk})

    def total_likes(self):
        return self.likes.count()


class Category(models.Model):
    'Model for categories in a post'
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
