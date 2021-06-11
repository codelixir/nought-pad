from django.urls import path
from .views import EditNoteView, HomeView, NoteView, AddNoteView, DeleteNoteView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('note/<int:pk>', NoteView.as_view(), name="note-details"),
    # <int:pk> => here pk is the primary key
    path('new_note/', AddNoteView.as_view(), name="add-note"),
    path('note/edit/<int:pk>', EditNoteView.as_view(), name="edit-note"),
    path('note/delete/<int:pk>', DeleteNoteView.as_view(), name="delete-note"),
]
