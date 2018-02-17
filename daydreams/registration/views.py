from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.template import RequestContext
from django.template import Context, Template
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from registration.forms import SignUpForm, InfoForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('welcome')
    else:
        form = SignUpForm()
    return render(request, 'index.html', {'form': form})

def forgot_pass(request):
    return render(request, 'forgot-password.html')

def welcome(request):
    return render(request, 'welcome.html')

def user_logout(request):
        logout(request)
        return render(request, 'logout.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username',)
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('info')
        else:
            return HttpResponse("Fuck you!")

    else:
        return render(request, 'login.html', {})

def info(request):
    if request.method == 'POST':
        form = InfoForm(data=request.POST or None,
                                   instance=request.user)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user.save()
            return redirect('welcome')

        else:
            form = InfoForm()

    return render(request, 'info.html', {})
