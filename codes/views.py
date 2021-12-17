from django.shortcuts import render, redirect

from accounts.models import Account
from .froms import CodeForm
from .models import SiteBanner, VerificationCode
from django.contrib.auth import  login
from idea.models import Idea_Bank
from about.models import Event
from django.contrib import messages
from .utils import sendSMS

def home(request): 

 
    best_idea = Idea_Bank.objects.filter( is_accepted = True).order_by("score").reverse()[0:3]
    banner = SiteBanner.objects.get(title = "m")
    events = Event.objects.all().order_by('created_at').reverse()[0:3]
    context = {
        "best_idea": best_idea,
        "banner" : banner,
        'events': events
    }
    return render(request, 'home.html', context)

def verification(request) : 

    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    


    if pk : 
       user = Account.objects.get(pk = pk)
       code = VerificationCode.objects.get(user= user)
       code_user = f"{code.number}"
       
    
       
       if not request.POST: 
          sendSMS(code_user, user.phone_number)
          print(code_user)
        
       if form.is_valid(): 
            num = form.cleaned_data.get('number')

            

            if str(code) == num : 
                code.save()
                messages.success(request, f"{user.first_name} {user.last_name} عزیز شما با موفقیت وارد شدید.")
                login(request, user)
                return redirect('home') 

            else :
                return redirect('login')

            

    context = {
        'form' : form
    }
    return render(request, 'verify.html', context)




def reset_verification(request) : 

    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    


    if pk : 
       user = Account.objects.get(pk = pk)
       code = VerificationCode.objects.get(user= user)
       code_user = f"{code.number}"
       
    
       
       if not request.POST: 
          sendSMS(code_user, user.phone_number)
          print(code_user)
        
       if form.is_valid(): 
            num = form.cleaned_data.get('number')

            

            if str(code) == num : 
                code.save()
                messages.success(request, f"{user.first_name} {user.last_name} عزیز رمز شما با موفقیت تغییر یافت.")
                request.session['pk'] = pk
                return redirect('changepassword') 

            else :
                return redirect('login')

            

    context = {
        'form' : form
    }
    return render(request, 'reset_verification.html', context)
