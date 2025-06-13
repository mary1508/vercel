from django.shortcuts import render

from django.http import HttpResponse

def newsView(request):
    return HttpResponse('Hola soy marycielo')
