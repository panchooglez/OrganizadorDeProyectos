from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Tarea

# Create your views here.
def home(request):
    return render(request, 'PanelDeControl/home.html')

def objetivos(request):
    tareas = Tarea.objects.all()
    return render(request, 'PanelDeControl/objetivos.html', {'tareas': tareas})

#Esto intuyo que no sera una buena practica incluirlo en views
def actualizar_tarea(request):
    if request.method == 'POST':
        id_tarea = request.POST.get('id')
        completada = request.POST.get('completed') == 'true'
        try:
            tarea = Tarea.objects.get(pk=id_tarea)
            tarea.completada = completada
            tarea.save()
            return JsonResponse({'success': True})
        except Tarea.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'No existe la tarea'}, status=404)
    return JsonResponse({'success': False, 'error': 'La request a esta url deberia ser un POST'}, status=400)

def despliegues(request):
    return render(request, 'PanelDeControl/despliegues.html')

def apis(request):
    return render(request, 'PanelDeControl/apis.html')
