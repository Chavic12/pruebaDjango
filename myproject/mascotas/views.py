from django.shortcuts import render, redirect
from .models import Adopcion


def home(request):
    return render(request, 'home.html')

def adopcion(request):
    return render(request, 'adopcion.html')

def personal(request):
    personal = Adopcion.objects.all()
    return render(request, 'personal.html', {'personal': personal})


def registrarPersonal(request):
    nombres = request.POST.get('nombre', False)
    apellidos = request.POST.get('apellido', False)
    correo = request.POST.get('correo', False)
    cedula = request.POST.get('cedula', False)
    direccion = request.POST.get('direccion', False)
    telefono = request.POST.get('telefono', False)

    personal = Adopcion.objects.create(nombres=nombres, apellidos=apellidos, correo=correo, cedula=cedula, direccion=direccion,telefono=telefono)
    return redirect('/home')


def eliminarPersonal(request, id):
    adopcion = Adopcion.objects.get(id=id)
    adopcion.delete()
    return redirect('/home')



