from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from base.models import Profile
# from base.models import Post


# Create your views here.

#it sends user to the signin page when not logged in, django feature
@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    return render(request,'index.html', {'user_profile': user_profile})

@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if request.FILES.get('image') == None:
            image = user_profile.profileimg

        else:
            image = request.FILES.get('image')

        bio = request.POST['bio']
        location = request.POST['location']

        user_profile.profileimg = image
        user_profile.bio = bio
        user_profile.location = location
        user_profile.save()
        
        
        return redirect('settings')
  
    return render(request,'setting.html', {'user_profile': user_profile })


@login_required(login_url='signin')
def upload(request):
    return HttpResponse('<h1>Upload View</h1>')


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #if two input passwords match
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'This username is taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email,password=password)
                user.save()

                #login user then redirect to settings page
                user_login = auth.authenticate(username=username,password=password)
                auth.login(request,user_login)
                

                #create Profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
                


        #if they do not match
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')


    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid login')
            return redirect('signin')
    else:
        return render(request,'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')



