from rest_framework import generics
from .models import Uclip_map
from .serializers import Uclip_mapSerializer
from django.shortcuts import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from django.http import HttpResponseBadRequest,JsonResponse

from rest_framework import viewsets

class UclipViewset(viewsets.ModelViewSet):
    queryset = Uclip_map.objects.all()
    serializer_class = Uclip_mapSerializer

# class Uclip_mapDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Uclip_map.objects.all()
#     serializer_class = Uclip_mapSerializer
   
    @action(detail=False, methods=['post','get'])
    @csrf_exempt
    def Uclip_data(self,request):
        if request.method == 'GET':
            data = request.GET.copy()
        elif request.method == 'POST':
            data = request.GET.copy()
        else:
            return HttpResponseBadRequest('Only POST and GET methods are supported')
        
        
        uclip_list = Uclip_map.objects.values()
        uclip_list = list(uclip_list)
        
        return JsonResponse(uclip_list, safe=False)

