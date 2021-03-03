from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse

class Index(View):
    def get(self, request):
        return render(request, 'edu/index.html', {'access': False})

class SignUp(View):
    def get(self, request):
        return render(request, 'edu/signUpForm.html')
    def post(self, request):
        data = {
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'password': make_password(request.POST.get('password'))
        }
        user = User(**data)
        user.save()
        return HttpResponse('Registered Successfully')

class SignIn(View):
    def get(self, request):
        return render(request, 'edu/signInForm.html', {'error': False})
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        has_access = bool(authenticate(username=username, password=password))
        if has_access:
            return render(request, 'edu/index.html', {'access': True})
        else:
            return render(request, 'edu/signInForm.html', {'error': True})


        
