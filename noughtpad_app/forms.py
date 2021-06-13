from django import forms
from django.forms import fields, widgets
from django.forms.models import ModelForm
from .models import Note


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'author', 'body']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'author': forms.TextInput(attrs={"class": "form-control", "id": "author_field", "type": "hidden"}),
            'body': forms.Textarea(attrs={"class": "form-control"})
        }


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'body': forms.Textarea(attrs={"class": "form-control"})
        }
