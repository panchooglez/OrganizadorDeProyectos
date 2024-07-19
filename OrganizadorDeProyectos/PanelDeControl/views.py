from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home')

def objetivos(request):
    return HttpResponse('Objetivos')

def despliegues(request):
    return HttpResponse('Despliegues')

def apis(request):
    return HttpResponse('Apis')
