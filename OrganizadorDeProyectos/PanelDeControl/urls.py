from django.urls import path
from PanelDeControl import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('objetivos', views.objetivos, name='Objetivos'),
    path('actualizar_tareas', views.actualizar_tarea, name='actualizar_tareas'), #Tiene que haber una mejor forma de organizar esta ruta
    path('despliegues', views.despliegues, name='Despliegues'),
    path('cambiar_despliegue', views.cambiar_despliegue, name='cambiar_despliegue'),
    path('apis', views.apis, name='Apis'),
]
