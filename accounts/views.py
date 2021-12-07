from django.shortcuts import render, redirect

from accounts.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from accounts.models import Account

def register(request ): 

    if request.method == "POST" : 

        form = RegistrationForm(request.POST)

        if form.is_valid(): 
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

            user = Account.objects.create_user(first_name = first_name, last_name = last_name, phone_number = phone_number, password = password)
            user.save()

            return redirect('login')
        
    else: 

        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request , 'register.html', context)


def login(request): 

    form = AuthenticationForm()
    if request.method == "POST":
        phone_number = request.POST.get('username')
        password = request.POST.get('password')

        print(phone_number)
        print(password)
        user = auth.authenticate(phone_number = phone_number, password = password)

        if user is not None: 
            request.session['pk'] = user.pk
            return redirect('verification')

        else: 
            print('login fiald')
            # django messages for error
            return redirect('login')

    context = {
        'form': form
    }  

    return render(request , 'login.html', context)


@login_required(login_url= 'login')
def logout(request ): 

    auth.logout(request)
    return redirect('login')
    

