from django.core.checks import messages
from django.shortcuts import redirect, render, get_object_or_404
from accounts.models import Account

from idea.forms import IdeaForm
from .models import Category, Idea_Bank
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages

def idea_view(request, pk = None): 

    categories = Category.objects.all()

    if pk != None:
        category = get_object_or_404(Category, pk = pk)
        idea = Idea_Bank.objects.filter(category = category, is_accepted = True)
        paginator = Paginator(idea, 6)
        page = request.GET.get('page')
        page_products = paginator.get_page(page)
        i_count = idea.count()

    else: 

        idea = Idea_Bank.objects.filter(is_accepted = True).order_by("created_at").reverse()
        paginator = Paginator(idea, 6)
        page = request.GET.get('page')
        page_products = paginator.get_page(page)
        i_count = idea.count()

    context = {
        'ideas': page_products,
        'categories': categories
    }
    return render(request, 'idea.html', context)

@login_required(login_url= 'login')
def idea_detail_view(request, category, pk):

    try: 
        category = Category.objects.get(pk = category)
        single_idea = get_object_or_404(Idea_Bank, category=  category, pk = pk)

    except: 
        pass

    context=  {
     "single_idea" : single_idea
    }
    return render(request, 'detail_view.html', context)



@login_required(login_url = 'login')
def send_idea(request): 
    
    if request.method == "POST" :
        form = IdeaForm(request.POST , request.FILES)
        
        if form.is_valid():
            user = request.user
            category = form.cleaned_data["category"]

            idea = Idea_Bank.objects.filter(user__exact = user, category__exact = category).exists()
            if idea: 
                messages.error(request,'شما از قبل در این رویداد ایده ثبت کرده اید.')
                return redirect('send_idea')
            # user = request.user
            # title = form.cleaned_data.get('title')
            # Category = form.cleaned_data.get('category')
            # desc = form.cleaned_data.get('desc')
            # participant_place = form.cleaned_data.get('participant_place')
            # contact = form.cleaned_data.get('contact')
            else:

                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                return redirect('idea_view')

        else: 
            #modal error
            print('error')


    else :
        form = IdeaForm()
        


    context = {
        'form': form
    }
    return render(request, 'send_idea.html', context)


def search(request) :
    if 'keyword' in request.GET: 
        keyword = request.GET['keyword']
        
        if keyword: 
            products = Idea_Bank.objects.filter(Q(desc__icontains = keyword) | Q(title__icontains=keyword))
            product_count = products.count()
            
    context = {
        "ideas" : products,
    }
    return render(request, 'idea.html', context)