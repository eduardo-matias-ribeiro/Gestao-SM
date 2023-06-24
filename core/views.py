from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from .forms import ContatosForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contatos(request):
    form = ContatosForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatosForm()
        else:
            messages.error(request, 'Erro ao enviar o e-mail, verifique os campos e tente novamente.')

    context ={
        'form': form
    }
    return render(request, 'contatos.html', context)
