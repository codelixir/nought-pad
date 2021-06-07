from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Note


class HomeView(ListView):
    'Render the Homepage'
    model = Note
    template_name = 'home.html'


class NoteView(DetailView):
    'Render a complete view of a Note'
    model = Note
    template_name = 'note_details.html'
