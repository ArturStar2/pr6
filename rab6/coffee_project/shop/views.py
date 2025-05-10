from django.shortcuts import render, redirect, get_object_or_404
from .models import Coffee
from .forms import CoffeeForm

def index(request):
    items = Coffee.objects.all()
    return render(request, 'shop/index.html', {'items': items})


def coffee_add(request):
    if request.method == 'POST':
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CoffeeForm()
    return render(request, 'shop/coffee_form.html', {'form': form})

def coffee_delete(request, pk):
    obj = get_object_or_404(Coffee, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('index')
    return render(request, 'shop/coffee_delete.html', {'item': obj})