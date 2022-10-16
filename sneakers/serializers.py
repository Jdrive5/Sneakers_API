from dataclasses import fields
from rest_framework import serializers
from .models import Sneaker

class Sneakerserializer(serializers.ModelSerializer):
    class Meta:
        model = Sneaker
        fields = ['id', 'title', 'description', 'price', 'inventory_quanity']