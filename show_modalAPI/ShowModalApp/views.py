from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt 
from django.core.files.storage import default_storage 

 
from .models import ObjModel
from .serializers import *


@api_view(['GET', 'POST'])
def objModel_list(request):
    """
 Массив со всеми текстурами
 """
    if request.method == 'GET':

        todos=ObjModel.objects.all() 
        dota_serializer=ObjModelSerializer(todos, many=True) 
        return JsonResponse(dota_serializer.data, safe=False)
    

    elif request.method == 'POST':
        serializer = ObjModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def objModel_detail(request, pk):
    """
    Удаление, обновление, получение данных об одной тудушки
    """
    print('pk',pk)
    try:

        firstStage = ObjModel.objects.get(article=pk)
        print('object',firstStage)
    except ObjModel.DoesNotExist:
        return Response(data='нету ничего',status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ObjModelSerializer(
            firstStage, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ObjModelSerializer(
            firstStage, data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        firstStage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@csrf_exempt
def SaveFile(request): 

    file=request.FILES['file'] 

    file_name=default_storage.save(file.name,file) 

    return JsonResponse(file_name,safe=False) 
