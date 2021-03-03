from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse


class Index(View):
    def get(self, request):
        return render(request, 'edu/index.html', {'access': request.user.is_authenticated})


class Register(View):
    def get(self, request):
        return render(request, 'edu/registration.html')

    def post(self, request):
        data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'password': make_password(request.POST.get('password1'))
        }
        user = User(**data)
        user.save()
        return render(request, 'edu/index.html', {'access': False})


class Login(View):
    def get(self, request):
        return render(request, 'edu/login.html', {'error': False})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'edu/index.html', {'access': True})
        else:
            return render(request, 'edu/login.html', {'error': True})


def logout_user(request):
    logout(request)
    return render(request, 'edu/index.html', {'access': False})
