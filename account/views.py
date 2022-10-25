from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.core.validators import validate_email
import re
from django.contrib.auth import login



def account(request) :
        if request.method == "POST" and 'login' in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user:
                if user is not None:
                    auth.login(request, user)
                return redirect('products')
            else:
                messages.info(request,'Invalid Credentials')
                return render(request,'account/account.html')
        else:
            return render(request, 'account/account.html')     
    

def reg(request) :
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Is Already Taken')
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Is Already Taken')
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            else:
                patt = '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$'
                if re.match(patt, email):
                    user = User.objects.create_user(
                    username=username, email=email, password=password)
                    user.save()
                    login(request, user)
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
                else: 
                    messages.info(request, 'Invaled Email')
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            return render(request, 'account/reg.html')



def logout(request):
    auth.logout(request)
    return redirect('/')