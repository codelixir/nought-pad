from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Note
from .forms import NoteForm


class HomeView(ListView):
    'Render the Homepage'
    model = Note
    template_name = 'home.html'


class NoteView(DetailView):
    'Render a complete view of a Note'
    model = Note
    template_name = 'note_details.html'


class AddNoteView(CreateView):
    'Add a new note'
    model = Note
    form_class = NoteForm
    template_name = 'add_note.html'
