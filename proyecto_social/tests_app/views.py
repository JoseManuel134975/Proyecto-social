from django.shortcuts import render, redirect, get_object_or_404
from .models import Test, Pregunta
from .forms import TestForm, PreguntaForm

# Create your views here.
def crear_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            test = form.save(commit=False)
            # test.autor = request.user
            test.save()
            return redirect('index')
    else:
        form = TestForm()
    
    return render(request, 'crear_test.html', {'form': form})

def agregar_pregunta(request, pk):
    test = get_object_or_404(Test, pk=pk)

    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            # test.autor = request.user
            pregunta.test = test
            pregunta.save()
            return redirect('index')
    else:
        form = PreguntaForm()
    
    return render(request, 'agregar_pregunta.html', {'form': form})

def ver_preguntas(request, pk):
    test = get_object_or_404(Test, pk=pk)
    preguntas = test.preguntas.all()

    return render(request, 'ver_preguntas.html', { 'preguntas': preguntas })
