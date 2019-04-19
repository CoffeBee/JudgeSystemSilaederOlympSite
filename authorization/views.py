from django.shortcuts import render, redirect
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if (request.user.is_authenticated):
        return  redirect('/programming')
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    print(request.POST)
    if form.is_valid():
        print(1)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')
