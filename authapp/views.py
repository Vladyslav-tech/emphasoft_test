from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import auth

from .forms import CustomerUserRegisterForm, CustomerUserEditForm, CustomerUserLoginForm


def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = CustomerUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = CustomerUserRegisterForm()

    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)



def login(request):
    title = 'Вход'
    login_form = CustomerUserLoginForm(data=request.POST or None)

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('auth:edit'))

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:main'))


def edit(request):
    title = 'Заполните профиль : '

    if request.method == 'POST':
        edit_form = CustomerUserEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('mainapp:main'))
    edit_form = CustomerUserEditForm(instance=request.user)
    content = {'title': title, 'edit_form': edit_form}
    return render(request, 'authapp/edit.html', content)