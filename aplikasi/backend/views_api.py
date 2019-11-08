from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics, filters, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            "Jajal Api": reverse('be:ini-api', request=request),
            "Test Electrical -> Turn Ratio": reverse('be:get-te-turn-ratio', request=request),
            # "-Get Predict aktual {before}": reverse('bp:predict-aktual-before', kwargs={'pk':30}, request=request),

        })

@api_view(['GET', 'POST'])
def get_te_turn_ratio(request):
    if request.method == 'GET':
        return JsonResponse('GET', safe=False)


    elif request.method == 'POST':
        return JsonResponse('POST', safe=False)
