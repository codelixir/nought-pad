from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, request
from django.contrib.auth.models import User
from .models import Category, Note, Profile
from .forms import AddNoteForm, EditNoteForm, EditProfileForm


def LikeView(request, pk):
    note = get_object_or_404(Note, id=request.POST.get('note_id'))
    user = request.user
    if note.likes.filter(id=user.id).exists():
        note.likes.remove(user)
    else:
        note.likes.add(user)
    return HttpResponseRedirect(reverse('note-details', args=[str(pk)]))


def UserNotesView(request, pk):
    author = get_object_or_404(User, id=pk)
    author_notes = Note.objects.filter(author=author)
    return render(request, 'user_notes.html', {'author': author, 'author_notes': author_notes})


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


class EditProfileView(UpdateView):
    'Edit the public profile'
    model = Profile
    template_name = 'edit_profile.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('home')

    def get_object(self):
        user = self.request.user
        if user.is_authenticated:
            return user.profile
        else:
            return None


class CreateProfileView(CreateView):
    'Edit the public profile when existing profile is blank'
    model = Profile
    template_name = 'edit_profile.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
