from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Tarefas
from .forms import tarefaForm

# Create your views here.
@login_required
def listaTarefa(request):
    tarefas_list = Tarefas.objects.all().order_by('-created_at').filter(usuario=request.user)

    search = request.GET.get('search')

    if search:
        tarefas = Tarefas.objects.filter(titulo__icontains=search, usuario=request.user)
        return render(request, 'tarefas/list.html', {'tarefas':tarefas})
    
    else:
      return render(request, 'tarefas/list.html', {'tarefas':tarefas_list})
@login_required
def tarefaView(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    return render(request, 'tarefas/tarefa.html', {'tarefa':tarefa})
@login_required
def novaTarefa(request):
    if request.method == 'POST':
        form = tarefaForm(request.POST)

        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.status = 'andamento'
            tarefa.usuario = request.user
            tarefa.save()
            return redirect('/')

    else:
        form = tarefaForm()
        return render(request, 'tarefas/addTarefas.html', {'form':form})
@login_required  
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
@login_required  
def deleteTarefa(request, id):
    tarefa = get_object_or_404(Tarefas, pk=id)
    tarefa.delete()
    return redirect('/')
