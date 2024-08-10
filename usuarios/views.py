from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

def login(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        Username = request.port.get('email')
        senha = request.POST.get('senha')

        User = authenticate(Username = Username,  password = senha)

        if User :
            login_django(request,User)
            return hasattr('Autenticado!')
        else:
            return HttpResponse('E-mail ou senha')
