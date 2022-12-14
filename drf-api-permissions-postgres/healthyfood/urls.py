from django.urls import path
from .views import HealthfoodListView,HealthfoodDetail,FoodtypeListView,FoodtypeDetailView
urlpatterns = [
   path('',HealthfoodListView.as_view(), name='thing_list'),
   path('<int:pk>',HealthfoodDetail.as_view(),name='thing_detail'),
   path('posts/',FoodtypeListView.as_view(), name='post_list'),
   path('posts/<int:pk>',FoodtypeDetailView.as_view(),name='post_detail')
]