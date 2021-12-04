from django.shortcuts import render, redirect

from accounts.models import Account
from .froms import CodeForm
from .models import VerificationCode
from django.contrib.auth import  login


def home(request): 
    return render(request, 'home.html')

def verification(request) : 

    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    

    if pk : 
       user = Account.objects.get(pk = pk)
       code = VerificationCode.objects.get(user= user)
       code_user = f"{user.phone_number}: {code.number}"
       
       if not request.POST: 
          print(code_user)
        
       if form.is_valid(): 
            num = form.cleaned_data.get('number')

            if str(code) == num: 
                code.save()
                login(request, user)
                return redirect('home')

            else :
                return redirect('login')

    context = {
        'form' : form
    }
    return render(request, 'verify.html', context)
