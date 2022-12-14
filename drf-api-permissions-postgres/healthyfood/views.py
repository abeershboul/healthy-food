from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import HealthyfoodSerializer,FoodSerializer
# Create your views here.
from .models import Food_type,Healthyfood
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
#from .permissions import AllowAny

# Create your views here.
class HealthfoodListView(ListCreateAPIView):
     queryset=Healthyfood.objects.all()
     serializer_class= HealthyfoodSerializer
     #permission_classes=[IsAuthenticatedOrReadOnly]

class HealthfoodDetail(RetrieveUpdateDestroyAPIView): 
    queryset=Healthyfood.objects.all()
    serializer_class= HealthyfoodSerializer 
    permission_classes=[IsOwnerOrReadOnly] 

class FoodtypeListView(ListCreateAPIView):
    queryset=Food_type.objects.all()
    serializer_class= FoodSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

class FoodtypeDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Food_type.objects.all()
    serializer_class= FoodSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
