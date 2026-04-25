from django.shortcuts import render

# Create your views here.
## ficheiro escola/views.py

from .models import Curso

##  ficheiro escola/views.py
from django.shortcuts import render
from .models import Curso

def cursos_view(request):

    cursos = (
        Curso.objects
        .select_related('professor')
        .prefetch_related('alunos')
        .all()
    )
    
    return render(request, 'escola/cursos.html', {'cursos': cursos})