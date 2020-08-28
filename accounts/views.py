from pyexpat.errors import messages
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
#from accounts.forms import UserForm, ProfileForm
from accounts.models import Profile
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import RegisterForm
"""
class SignUp(generic.CreateView):
    form_class = ProfileCreationForm
    success_url = '/'
    template_name = 'accounts/signup.html'
"""

def signup(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit = False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            return render(request, 'accounts/login.html', {'user': user})

            #authenticated_user = authenticate(username=new_user.username,
            #                                  password=request.POST['password1'])
            #auth.login(request, authenticated_user)
            #return HttpResponseRedirect(reverse('login'))
            #return redirect('accounts:login')
    elif request.method == 'GET':
        user_form = RegisterForm()
    return render(request, 'accounts/signup.html', {'user_form': user_form})


def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth.login(request, request.user)
            return redirect('/')
    else:
        login_form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'login_form': login_form})

    """
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                auth.login(request, user)
                return redirect('/')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'accounts/login.html', {'login_form': login_form})

    """

def logout(request):
    auth.logout(request)
    return redirect('posts:list')

"""
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"])
            nickname = request.POST["nickname"]
            profile = Profile(user=user, nickname=nickname)
            profile.save()
            auth.login(request,user)
            return redirect('accounts:login')
    return render(request, 'accounts/signup.html')
"""
"""
@login_required
@transaction.atomic

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:login')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
"""

def loginmain(request):
    return render(request, 'account/login_main.html')