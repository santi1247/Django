from django.db import models
from jugadores.models import Jugador

class Cuota(models.Model):
    idCuota=models.AutoField(primary_key=True,verbose_name="idCuota",db_column='idCuota')
    id=models.ForeignKey(Jugador,on_delete=models.CASCADE,verbose_name="id")
    nom= models.CharField(max_length=50,verbose_name="Nombre y Apellido")
    cuotaMes=models.DateField(verbose_name="Cuota Mes")
    fechap=models.DateField(verbose_name="Fecha de Pago")
    importe=models.FloatField(max_length=10,verbose_name="importe")
    
    def __str__(self):
        fila=str(self.idCuota)+"-"+str(self.id)+"-"+self.nom
        return fila
