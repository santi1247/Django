from django.shortcuts import render, redirect
from django.http import HttpResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .forms import EventoForm, OrganizadorForm
from evento.models import Evento, Organizador

# Create your views here

def listaEvento(request):
    eventos=Evento.objects.all()
    return render(request,"crudEvento/listado.html",{'eventos':eventos})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

def crear_editarEvento(request,idEvento=0):
      if request.method=="GET":# CREA UN FORMULARIO VACIO
        if idEvento==0:
            formulario=EventoForm()   
        else:
            eventoid=Evento.objects.get(pk=idEvento)
            formulario=EventoForm(instance=eventoid)
        return render(request,'crudEvento/Crear.html',{'formulario':formulario})
      else:#, se busca el evento existente y se vincula al formulario con los datos enviados.

        if idEvento==0:#Si idEvento es 0, se crea un formulario con los datos enviados (request.POST y request.FILES).
            formulario=EventoForm(request.POST or None, request.FILES or None)
        else:
            eventoid=Evento.objects.get(pk=idEvento)
            formulario=EventoForm(request.POST or None, request.FILES or None ,instance=eventoid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaEvento')
        
def eliminaEvento(request, idEvento):
    bc=Evento.objects.get(pk=idEvento)
    bc.delete()
    return redirect('listaEvento')
        

def listaOrganizador(request):
    organizadores=Evento.objects.all()
    return render(request,"crudEvento/listado.html",{'organizadores':organizadores})

 

def crear_editarOrganizador(request,idOrganizador=0):
      if request.method=="GET":# CREA UN FORMULARIO VACIO
        if idOrganizador==0:
            formulario=OrganizadorForm()   
        else:
            organizadorid=Organizador.objects.get(pk=idOrganizador)
            formulario=OrganizadorForm(instance=organizadorid)
        return render(request,'crudEOrganizador/Crear.html',{'formulario':formulario})
      else:#, se busca el evento existente y se vincula al formulario con los datos enviados.

        if idEvento==0:#Si idEvento es 0, se crea un formulario con los datos enviados (request.POST y request.FILES).
            formulario=OrganizadorForm(request.POST or None, request.FILES or None)
        else:
            organizadorid=Organizador.objects.get(pk=idEvento)
            formulario=OrganizadorForm(request.POST or None, request.FILES or None ,instance=organizadorid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaOrganizador')
        
def eliminaOrganizador(request, idOrganizador):
    bc=Organizador.objects.get(pk=idOrganizador)
    bc.delete()
    return redirect('listaEOrganizador')        