from socket import fromshare
from django import forms 
from .models import Jugador

class JugadorForm(forms.ModelForm):
  class Meta:
        model=Jugador
       #fields='__all__'
        fields=('DNI','nom','fechan','altura',"peso","dire","cd","talla","descripcion")
        labels ={
            "DNI" : "DNI del jugador" ,
            'nom': 'nombre y apellido del jugador:',
            "fechan" : "fehca de nacimiento del jugador" ,
            "altura" : "altura del jugador" ,
            "peso" : "peso del jugador" , 
            "dire" : "direccion del jugador",
            "cd" : "codigo postal del jugador",
            "talla" : "talla de indumentaria ",
            "descripcion" : "Deporte al que pertenece el jugador",
          #  "nummac" : "numero de macc " ,
           
                   
        
        }
        
    
  def __init__(self, *args, **kwargs):
        super(JugadorForm,self).__init__(*args,**kwargs)
        self.fields['descripcion'].empty_label="Selecciona"
        self.fields['nom'].required=True
        self.fields['fechan'].required=False
        