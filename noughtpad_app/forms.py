from django import forms
from django.forms import fields, widgets
from django.forms.models import ModelForm
from .models import Note


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        # fields = ['title', 'author', 'body']
        fields = ['title', 'author', 'body', 'banner']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control col-9"}),
            'author': forms.TextInput(attrs={"class": "form-control", "id": "author_field", "type": "hidden"}),
            'body': forms.Textarea(attrs={"class": "form-control"})
        }


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        # fields = ['title', 'body']
        fields = ['title', 'body', 'banner']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control col-9"}),
            'body': forms.Textarea(attrs={"class": "form-control"})
        }
