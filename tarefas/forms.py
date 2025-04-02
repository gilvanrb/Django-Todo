from django import forms

from .models import Tarefas

class tarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefas
        fields = ('titulo', 'descricão')