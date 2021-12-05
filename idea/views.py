from django.shortcuts import render, get_object_or_404
from .models import Category, Idea

def idea_view(request): 

    ideas = Idea.objects.all().order_by("created_at").reverse()

    context = {
        'ideas': ideas
    }
    return render(request, 'idea.html', context)


def idea_detail_view(request, category, pk):

    try: 
        category = Category.objects.get(pk = category)
        single_idea = get_object_or_404(Idea, category=  category, pk = pk)

    except: 
        pass

    context=  {
     "single_idea" : single_idea
    }
    return render(request, 'detail_view.html', context)