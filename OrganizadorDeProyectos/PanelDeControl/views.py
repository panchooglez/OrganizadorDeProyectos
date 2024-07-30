import subprocess
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, 'PanelDeControl/home.html')

def objetivos(request):
    tareas = Tarea.objects.all()
    return render(request, 'PanelDeControl/objetivos.html', {'tareas': tareas})

def cambiar_despliegue(request):
    id = request.POST.get('id')
    nuevo_valor = request.POST.get('desplegada') == 'true'
    ruta_despliegue = request.POST.get('ruta_despliegue')

    try:
        instancia = Despliegue.objects.get(id=id)
        instancia.desplegada = nuevo_valor
        instancia.save()
        state = "up" if nuevo_valor else "down"
        #f"docker compose -f {ruta_despliegue} {state} -d"
        resultado = subprocess.run(f"docker compose -f {ruta_despliegue} {state} -d", shell=True, capture_output=True, text=True)
        print('stdout: ' + resultado.stdout)
        print('stderr: ' + resultado.stderr)
        return JsonResponse({'success': True, 'stdout': resultado.stdout, 'stderr': resultado.stderr})
    except Despliegue.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Error en despliegue'}, status=404)

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
    despliegues = Despliegue.objects.all()
    return render(request, 'PanelDeControl/despliegues.html', {'despliegues': despliegues})

def apis(request):
    return render(request, 'PanelDeControl/apis.html')
