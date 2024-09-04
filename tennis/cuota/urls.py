from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static



urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('cuota/listaCuota',views.listaCuota,name='listaCuota'),
    path('cuota/<int:idCuota>/', views.crear_editarCuota, name='crear_editarCuota'),
    path('eliminarCuota/<int:idCuota>/',views.eliminaCuota,name='eliminaCuota'),  

    
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)