from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return JsonResponse('ok', safe=False)

def ini_api(request):
    return JsonResponse('ini api', safe=False)
