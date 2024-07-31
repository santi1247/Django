from django.db import models

class Deporte(models.Model):
    descripcion=models.CharField(max_length=50,verbose_name="descripcion")
    
    def __str__(self):
      fila=self.descripcion
      return fila
    
# Create your models here.
class Jugador(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    DNI=models.IntegerField(verbose_name="DNI")
    nom = models.CharField(max_length=50,verbose_name="Nombre y Apellido")
    fechan=models.DateField(verbose_name="Fecha Nacimiento")
    altura=models.FloatField(max_length=3,verbose_name="Altura")
    peso=models.FloatField(max_length=3,verbose_name="Peso")
    dire=models.CharField(max_length=50,verbose_name="Direccion")
    cd=models.CharField(max_length=6,verbose_name="codigo postal")
    talla=models.CharField(max_length=6,verbose_name="numero de talla indumentaria")
    descripcion=models.ForeignKey(Deporte, verbose_name="descripcion", on_delete=models.CASCADE)
    
    
    def __str__(self):
        fila=str(self.id)+"-"+str(self.DNI)+"-"+self.nom
        return fila
    


    