from django.urls import path
from PanelDeControl import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('objetivos', views.objetivos, name='Objetivos'),
    path('despliegues', views.despliegues, name='Despliegues'),
    path('apis', views.apis, name='Apis'),
]
