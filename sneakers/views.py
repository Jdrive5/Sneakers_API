from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Sneakerserializer
from .models import Sneaker
from sneakers import serializers

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

@api_view(['GET'])
def sneaker_detail(request, pk):
    try:
        sneaker = Sneaker.objects.get(pk=pk)
        serializer = Sneakerserializer(sneaker);
        return Response(serializer.data)

    except Sneaker.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND);
