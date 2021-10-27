from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product
from .forms import Productform

def home(request):
    search = request.GET.get('search')
    if search:
        products = Product.objects.filter(title__icontains=search)
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def newProduct(request):
    if request.method == 'POST':
        form = Productform(request.POST)
        if form.is_valid():
            product = form.save()
            messages.info(request, 'Produto adicionado com sucesso')
            return redirect('/')
    else:
        form = Productform()
        return render(request, 'products/addProduct.html', {'form': form})

def edit(request, id):
    product = get_object_or_404(Product, pk=id)
    form = Productform(instance=product)
    if request.method == 'POST':
        form = Productform(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'Produto atualizado com sucesso')
            return redirect('/')
        else:
            return render(request, 'products/edit.html', {'product': product, 'form': form})
    else:
        return render(request, 'products/edit.html', {'product': product, 'form': form})

def delete(request, id):
    task = get_object_or_404(Product, pk=id)
    task.delete()
    messages.info(request, 'Produto deletado com sucesso')
    return redirect('/')