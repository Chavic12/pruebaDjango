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


def eliminarPersonal(request, pk):
    adopcion = Adopcion.objects.get(id=pk)
    adopcion.delete()
    return redirect('/personal')


def edicionPersonal(request, pk):
    adopcion = Adopcion.objects.get(id=pk)
    return render(request, 'editar.html', {'adopcion': adopcion})

def editarPersonal(request):
    pk = request.POST.get('s_id')
    adopcion = Adopcion.objects.get(id=pk)
    adopcion.nombres = request.POST.get('nombre', False)
    adopcion.apellidos = request.POST.get('apellido', False)
    adopcion.correo = request.POST.get('correo', False)
    adopcion.cedula = request.POST.get('cedula', False)
    adopcion.direccion = request.POST.get('direccion', False)
    adopcion.telefono = request.POST.get('telefono', False)
    
    adopcion.save()
    return redirect('/personal')




