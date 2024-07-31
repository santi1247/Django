from socket import fromshare
from django import forms 
from .models import Cuota


class CuotaForm(forms.ModelForm):
  class Meta:
        model=Cuota
       #fields='__all__'
        fields=('idCuota','id','nom','cuotaMes','fechap',"importe")
        labels ={
          
            "idCuota":" id cuota",
            "id" : "Jugador" ,
            'nom': 'nombre y apellido del jugador:',
            "cuotaMes":"Mes al que corresponde la cuota",
            "fechap" : "fecha de pago" ,
            "importe" : "valor cuota" ,

          #  "nummac" : "numero de macc " ,
           
                   
        
        }
        
    
  def __init__(self, *args, **kwargs):
        super(CuotaForm,self).__init__(*args,**kwargs)
        
       
        self.fields['cuotaMes']
        self.fields['nom'].empty_label="Selecciona"
       # self.fields['nom'].required=True
        self.fields['fechap'].required=False
        