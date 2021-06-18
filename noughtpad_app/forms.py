from django import forms
from django.forms import fields, widgets
from django.forms.models import ModelForm
from .models import Note, Profile


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'author', 'body', 'banner']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control col-9"}),
            'author': forms.TextInput(attrs={"class": "form-control", "id": "author_field", "type": "hidden"}),
            'body': forms.Textarea(attrs={"class": "form-control"})
        }


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body', 'banner']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control col-9"}),
            'body': forms.Textarea(attrs={"class": "form-control"})
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['about', 'profile_pic', 'website', 'facebook',
                  'twitter', 'instagram', 'github', 'linkedin', 'link']
        widgets = {
            'about': forms.Textarea(attrs={"class": "form-control col-9", "rows": 3}),
            'website': forms.TextInput(attrs={"class": "form-control col-9"}),
            'facebook': forms.TextInput(attrs={"class": "form-control col-9"}),
            'twitter': forms.TextInput(attrs={"class": "form-control col-9"}),
            'instagram': forms.TextInput(attrs={"class": "form-control col-9"}),
            'github': forms.TextInput(attrs={"class": "form-control col-9"}),
            'linkedin': forms.TextInput(attrs={"class": "form-control col-9"}),
            'link': forms.TextInput(attrs={"class": "form-control col-9"}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["link"].label = "Any Other Link"
