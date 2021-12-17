from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404, render, redirect

from accounts.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from accounts.models import Account
from django.contrib import messages
from idea.models import Idea_Bank
from idea.forms import IdeaForm

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
            messages.error(request, 'کاربر گرامی ثبت نام شما انجام نشد مجدادا تلاش بفرمایید')
        
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

        user = auth.authenticate(phone_number = phone_number, password = password)

        if user is not None: 
            request.session['pk'] = user.pk
            return redirect('verification')

        else: 
            messages.error(request, 'شماره همراه یا نام کاربری نادرست است.')
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
    

@login_required(login_url='login')
def dashboard(request) :
    user = request.user
    user_idea = Idea_Bank.objects.filter(user__exact = user)

    context = {

        'user_idea' : user_idea
    }

    return render(request, 'dashboard.html', context)


@login_required(login_url='login') 
def delete_idea(request, pk) : 
    user = request.user
    idea = get_object_or_404(Idea_Bank, pk=pk)

    if idea.user == user : 
        idea.delete()
        return redirect('dashboard')
    else: 
        messages.error(request, "شما دسترسی برای حذف ایده را ندارید.")
        return redirect('logout')

@login_required(login_url='login')
def edit_idea(request, pk) :
    user = request.user
    idea = get_object_or_404(Idea_Bank, pk=pk)

    if idea.user == user : 
        if request.method == "POST": 
            form = IdeaForm(request.POST,request.FILES, instance = idea)
            if form.is_valid() :
                form.save()
                return redirect('dashboard')
            else :
                messages.error(request, "فرم را به درستی تکمبل نکردید !")
            

        else:
            form = IdeaForm(instance = idea)
    
    else :
        messages.error(request, "شما دسترسی برای حذف ایده را ندارید.")
        return redirect('logout')

    context = {
        'form' : form
    }  

    return render(request, 'edit_idea.html', context)


def forgot_password(request) :

    if request.method == "POST" : 
        phone_number = request.POST["phone_number"]

        user = Account.objects.get(phone_number__exact = phone_number)
        print(user.pk)
        if user is not None:
           
            request.session['pk'] = user.id
            return redirect('reset_verification')

    return render(request, 'forgotpassword.html')


def changepassword(request) :
    pk = request.session['pk']
    user = Account.objects.get(pk = pk)

    if request.method == "POST" : 
        new_pass = request.POST["newpass"]

        user.set_password(new_pass)
        user.save()
        return redirect('login')
    
    return render(request, 'change_password.html')


# @login_required(login_url='login')
# def account_info(request) :

#     user = request.user
#     if request.method == "POST" : 
    
#         form = RegistrationForm(request.POST, instance = user)

#         if form.is_valid() :
#             form.save()
#             return redirect('dashboard')
#         else :
#             messages.error(request, "فرم را به درستی تکمبل نکردید !")


#     else:
#         form = RegistrationForm(instance = user)
        

#     context = {
#         'form' : form
#     }
#     return render(request, 'account_info.html', context)