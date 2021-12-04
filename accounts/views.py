from django.shortcuts import render, redirect

from accounts.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def register(request ): 

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
    return render(request , 'logout.html')

