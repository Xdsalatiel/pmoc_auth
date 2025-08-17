from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Equipamento
from .forms import EquipamentoForm

@login_required
def listar_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamentos/listar.html', {'equipamentos': equipamentos})

@login_required
def adicionar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_equipamentos')
    else:
        form = EquipamentoForm()
    return render(request, 'equipamentos/form.html', {'form': form})

@login_required
def editar_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('listar_equipamentos')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamentos/form.html', {'form': form})

@login_required
def remover_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        return redirect('listar_equipamentos')
    return render(request, 'equipamentos/remover.html', {'equipamento': equipamento})
