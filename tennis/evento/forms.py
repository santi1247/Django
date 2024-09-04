from socket import fromshare
from django import forms 
from .models import Evento, Organizador


class EventoForm(forms.ModelForm):
  class Meta:
        model=Evento
       #fields='__all__'
        fields=('idEvento','nom','fecha','ubicacion',"idOrganizador")
        labels ={
          
            "idEvento":" id Evento",
            'nom': 'nombre del Evento:',
            "fecha":"Fecha Evento",
            "ubicacion" : "ubicación " ,
            "idOrganizador" : "Id Organizador" ,
  
        
        }
        
    
  def __init__(self, *args, **kwargs):
        super(EventoForm,self).__init__(*args,**kwargs)
        
        self.fields['fecha']
        self.fields['nom'].empty_label="Selecciona"
       # self.fields['nom'].required=True
        self.fields['idOrganizador'].required=False
        
 
class OrganizadorForm(forms.ModelForm):
  class Meta:
        model=Organizador
       #fields='__all__'
        fields=('idOrganizador','nom','contacto')
        labels ={
          
            "idOrganizador":" Código organizador",
            'nom': 'nombre de Organizador:',
            "contacto":"Contacto",
           
  
        
        }
        
    
  def __init__(self, *args, **kwargs):
        super(EventoForm,self).__init__(*args,**kwargs)
        
        self.fields['idOrganizador']
        self.fields['nom'].empty_label="Selecciona"
       # self.fields['nom'].required=True
    #    self.fields['idOrganizador'].required=False
               