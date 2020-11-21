from django import forms
from notes.models import Note

class NoteModelForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('author', 'recipent', 'content', 'importance')