from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static



urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('evento/listaEvento',views.listaEvento,name='listaEvento'),
    path('evento/crear_editarEvento/<int:idEvento>/', views.crear_editarEvento, name='crear_editarEvento'),
    path('eliminarEvento/<int:idEvento>/',views.eliminaEvento,name='eliminaEvento'),  
    path('evento/listaOrganizador',views.listaOrganizador,name='listaOrganizador'),
    path('evento/crear_editarOrganizador/<int:idOrganizador>/', views.crear_editarOrganizador, name='crear_editarOrganizador'),
    path('eliminarEvento/<int:idOrganizador>/',views.eliminaOrganizador,name='eliminaOrganizador'),  


      
 
 
 
 
    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)