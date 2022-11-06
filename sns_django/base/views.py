from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from base.models import Profile

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #if two input passwords match
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'This username is taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email,password=password)
                user.save()

                #login user then redirect to settings page
                

                #create Profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
                


        #if they do not match
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')


    else:
        return render(request, 'signup.html')

def signin(request):
    return render(request,'signin.html')