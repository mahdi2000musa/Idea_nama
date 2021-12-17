from django.urls import path
from . import views

urlpatterns = [
    path('', views.about,  name = 'about' ),
    path('events/', views.events, name="events"),
    path('under-construction/', views.under_construction, name="under-construction")

]