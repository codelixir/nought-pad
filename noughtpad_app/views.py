#from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Note
from .forms import AddNoteForm, EditNoteForm


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
    form_class = AddNoteForm
    template_name = 'add_note.html'


class EditNoteView(UpdateView):
    'Edit an existing note'
    model = Note
    form_class = EditNoteForm
    template_name = 'edit_note.html'
