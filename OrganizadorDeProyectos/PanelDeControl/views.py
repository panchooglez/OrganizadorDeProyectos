from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'PanelDeControl/home.html')

def objetivos(request):
    return render(request, 'PanelDeControl/objetivos.html')

def despliegues(request):
    return render(request, 'PanelDeControl/despliegues.html')

def apis(request):
    return render(request, 'PanelDeControl/apis.html')
