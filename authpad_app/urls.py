from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePassView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('password/', ChangePassView.as_view(), name="change-pass"),
    path('settings/', UserEditView.as_view(), name="settings"),
]
