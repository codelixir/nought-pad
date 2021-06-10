from django.urls import path
from .views import HomeView, NoteView, AddNoteView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('note/<int:pk>', NoteView.as_view(), name="note-details"),
    # <int:pk> => here pk is the primary key
    path('new_note/', AddNoteView.as_view(), name="add-note")
]
