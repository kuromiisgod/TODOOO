from django import forms
from todo_app.models import TodoOne

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoOne
        fields = ('memo','url')