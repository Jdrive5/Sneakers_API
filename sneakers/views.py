from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Sneakerserializer
from .models import Sneaker

@api_view(['GET', 'POST'])
def sneakers_list(request):
    if request.method == 'GET':
        sneakers = Sneaker.objects.all()
        serializer = Sneakerserializer(sneakers, many=True)
        return Response(serializer.data)   
    elif request.method == 'POST':
        serializer = Sneakerserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def sneaker_detail(request, pk):
    sneaker = get_object_or_404(Sneaker, pk=pk)
    if request.method == 'GET':     
        serializer = Sneakerserializer(sneaker);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Sneakerserializer(sneaker, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
