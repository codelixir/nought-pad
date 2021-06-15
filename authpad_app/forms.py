from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['username', 'first_name', 'last_name',
                      'email', 'password1', 'password2']:
            self.fields[field].widget.attrs['class'] = "form-control col-5"

        self.fields['password1'].help_text = "Your password must contain at least 8 characters and can’t be entirely numeric."


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['username', 'first_name', 'last_name', 'email']:
            self.fields[field].widget.attrs['class'] = "form-control col-5"

        self.fields['password'].help_text = "You can change the password using <a href='../password/'>this form</a>."
