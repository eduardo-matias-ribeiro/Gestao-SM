from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContatosForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contatos(request):
    form = ContatosForm()

    context ={
        'form': form
    }
    return render(request, 'contatos.html', context)
