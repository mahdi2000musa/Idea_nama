from django.shortcuts import render
from .models import Event

def about(request):

    return render(request, 'about.html')


def events(request) : 
    events = Event.objects.all().order_by("created_at").reverse()

    context = {
        'events': events,
    }
    return render(request, 'events.html', context)


def under_construction(request):
    
    return render(request, 'under_construct.html')