from django.shortcuts import render, redirect
from django.http import HttpResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .forms import CuotaForm
from cuota.models import Cuota

# Create your views here

def listaCuota(request):
    cuotas=Cuota.objects.all()
    return render(request,"crudCuotas/listado.html",{'cuotas':cuotas})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

def crear_editarCuota(request,idCuota=0):
      if request.method=="GET":
        if idCuota==0:
            formulario=CuotaForm()   
        else:
            cuotaid=Cuota.objects.get(pk=idCuota)
            formulario=CuotaForm(instance=cuotaid)
        return render(request,'crudCuotas/Crear.html',{'formulario':formulario})
      else:
        if idCuota==0:
            formulario=CuotaForm(request.POST or None, request.FILES or None)
        else:
            cuotaid=Cuota.objects.get(pk=idCuota)
            formulario=CuotaForm(request.POST or None, request.FILES or None ,instance=cuotaid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listaCuota')
        
def eliminaCuota(request, idCuota):
    bc=Cuota.objects.get(pk=idCuota)
    bc.delete()
    return redirect('listaCuota')
        