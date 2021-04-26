from django.shortcuts import render, redirect
from. models import Curso, Descripcion
from django.contrib import messages

def cursos(request):
    context = {
        "cursos" : Curso.objects.all(),
        "description": Descripcion.objects.all()
    }
    return render(request, "cursos.html", context)


def agregar_curso(request):

    errors = Curso.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/")


    name_from_form = request.POST["name"]
    description_from_form = request.POST['description']
    Descripcion.objects.create(description = description_from_form)
    descripcion = Descripcion.objects.last()
    nuevo_curso = Curso.objects.create(
        name=name_from_form,
        description = descripcion
          
    )
    
    return redirect("/")

def eliminar_curso(request, idCurso):

    curso = Curso.objects.get(id=idCurso)
    context = {
        "curso" :curso
    }

    return render(request, "eliminar_curso.html", context)

def eliminar(request, idCurso):
    
    curso_to_delete = Curso.objects.get(id=idCurso)
    curso_to_delete.delete()

    return redirect("/")


