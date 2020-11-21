from django.shortcuts import render
from notes.models import Note
from .forms import NoteModelForm
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    notes = Note.objects.order_by('-importance', '-created')
    form = NoteModelForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context = {
        'form': form,
        'notes': notes,
    }
    return render(request, 'main/index.html', context)

def delete(request):
    if request.method == "POST":
        obj = Note.objects.get(id=request.POST['note-id'])
        obj.delete()
    return HttpResponseRedirect('/')