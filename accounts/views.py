from django.shortcuts import render

from accounts.forms import RegistrationForm



def register(request ): 

    form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request , 'register.html', context)


def login(request ): 
    return render(request , 'login.html')


def logout(request ): 
    return render(request , 'logout.html')