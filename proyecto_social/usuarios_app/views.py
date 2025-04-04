from django.shortcuts import render, redirect
from usuarios_app.forms import RegistroForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from tests_app.models import Test


# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form} )


@login_required
def index(request):
    tests = Test.objects.all()
    
    return render(request, 'index.html', { 'tests': tests })


def salir(request):
    logout(request)
    return redirect('login')

