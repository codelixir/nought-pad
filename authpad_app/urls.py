from django.urls import path
from .views import UserRegisterView, UserEditView, ChangePassView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit-profile"),
    path('password/', ChangePassView.as_view(), name="change-pass"),

]
