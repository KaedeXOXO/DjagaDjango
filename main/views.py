from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Hardware
from .forms import HardwareForm

def index(request):
    hardware = Hardware.objects.all()
    return render(request, 'main/index.html', {
        'title': 'Каталог',
        'hardware': hardware
    })

def index_tab(request):
    hardware = Hardware.objects.order_by('-id')
    return render(request, 'main/index_tab.html', {
        'title': 'Каталог',
        'hardware': hardware
    })

def about(request):
    return render(request, 'main/about.html')


def create(request):
    if request.method == 'POST':
        form = HardwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    form = HardwareForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

def hardware_edit(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = HardwareForm()
        else:
            hardware = Hardware.objects.get(id=id)
            form = HardwareForm(instance=hardware)
        return render(request, 'main/hardware_edit.html', {'form': form})

    else:
        if id == 0:
            form = HardwareForm(request.POST)
        else:
            hardware = Hardware.objects.get(id=id)
            form = HardwareForm(request.POST, instance=hardware)
        if form.is_valid():
            form.save()
            return redirect('main')

def hardware_view(request, id=1):
    try:
        hardware = Hardware.objects.get(id=id)
    except Hardware.DoesNotExist:
        raise Http404
    return render(request, 'main/hardware_view.html', {
        'title': 'Товар',
        'hardware': hardware
    })

def hardware_delete(request, id=0):
    try:
        hardware = Hardware.objects.get(id=id)
        hardware.delete()
    except Hardware.DoesNotExist:
        raise Http404
    hardware = Hardware.objects.order_by('-id')
    return render(request, 'main/index_tab.html', {
        'title': 'Каталог',
        'hardware': hardware
    })