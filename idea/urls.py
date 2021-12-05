from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.idea_view, name= "idea_view"),
    path('<int:category>/<int:pk>/', views.idea_detail_view, name= "detail_view"),
    
]