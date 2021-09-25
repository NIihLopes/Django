# Create your views here.
from .models import transacao
from django.shortcuts import render
from .form import TransacaoForm
import datetime


def home(request):
    data = {}
    data['transacoes'] = ['ti','t2','t3']
    data['now'] = datetime.datetime.now()
    #html = "<html><body>agora são %s.</body></html>" % now
    return render(request,'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = transacao.objects.all()
    return render(request,'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return listagem(request)
    data['form'] = form

    return render(request,'contas/form.html', data)