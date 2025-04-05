from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefas
from .forms import tarefaForm

# Create your views here.

def listaTarefa(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at')

    search = request.GET.get('search')

    if search:
        tarefas = Tarefas.objects.filter(titulo__icontains=search)
        return render(request, 'tarefas/list.html', {'tarefas':tarefas})
    
    else:
      return render(request, 'tarefas/list.html', {'tarefas':tarefas_list})

def tarefaView(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    return render(request, 'tarefas/tarefa.html', {'tarefa':tarefa})

def novaTarefa(request):
    if request.method == 'POST':
        form = tarefaForm(request.POST)

        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.status = 'andamento'
            tarefa.save()
            return redirect('/')

    else:
        form = tarefaForm()
        return render(request, 'tarefas/addTarefas.html', {'form':form})
    
def editTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    form = tarefaForm(instance=tarefa)

    if request.method == 'POST':
        form = tarefaForm(request.POST, instance=tarefa)

        if form.is_valid():
            tarefa.save()
            return redirect('/')
        else:
            return render(request, 'tarefas/editTarefa.html', {'form': form, 'tarefa': tarefa})

    else:
        return render(request, 'tarefas/editTarefa.html', {'form': form, 'tarefa': tarefa})
    
def deleteTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    tarefa.delete()
    return redirect('/')
