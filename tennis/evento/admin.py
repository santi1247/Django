
from django.contrib import admin
from .models import *
from .models import Evento, Organizador

# Register your models here.


admin.site.register(Evento)
admin.site.register(Organizador)
