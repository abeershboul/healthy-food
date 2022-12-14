from rest_framework import serializers

from .models import Healthyfood,Food_type
class  HealthyfoodSerializer(serializers.ModelSerializer):
    class Meta:
        model= Healthyfood
       
        fields='__all__'
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model= Food_type
        fields='__all__'        