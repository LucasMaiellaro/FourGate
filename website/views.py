from django.shortcuts import render
from website.forms import CarroForm
from website.models import *

# Create your views here.

def landing(request):
    return render (request, 'landing.html')

def home(request):
    return render(request, 'home.html')


def cadastro_carro(request):
    form = CarroForm(request.POST or None)
  
    if form.is_valid():
        form.save()
        context = {
            'msg': 'Carro cadastrado com sucesso!'
        }
        return render(request, 'cadastro.html', context)
    
    context = {
        'formulario': form
    }
    
    return render(request, 'cadastro.html', context)