from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Category, Note
from .forms import AddNoteForm, EditNoteForm


def LikeView(request, pk):
    note = get_object_or_404(Note, id=request.POST.get('note_id'))
    user = request.user
    if note.likes.filter(id=user.id).exists():
        note.likes.remove(user)
    else:
        note.likes.add(user)
    return HttpResponseRedirect(reverse('note-details', args=[str(pk)]))


class HomeView(ListView):
    'Render the Homepage'
    model = Note
    template_name = 'home.html'
    ordering = ['-timestamp']


class NoteView(DetailView):
    'Render a complete view of a Note'
    model = Note
    template_name = 'note_details.html'

    def get_context_data(self, *args, **kwargs):
        note = get_object_or_404(Note, id=self.kwargs['pk'])
        liked = True if note.likes.filter(
            id=self.request.user.id).exists() else False
        context_data = super(NoteView, self).get_context_data(*args, **kwargs)
        context_data["categories"] = [cat for cat in Category.objects.all()]
        context_data["total_likes"] = note.total_likes()
        context_data["like_button"] = "btn-primary" if liked else "btn-outline-primary"

        return context_data


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


class DeleteNoteView(DeleteView):
    'Delete a note'
    model = Note
    template_name = 'delete_note.html'
    success_url = reverse_lazy('home')
