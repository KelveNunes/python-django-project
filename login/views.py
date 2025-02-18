from django.shortcuts import render


def login(request):
    return render(request, 'login/login.html')

def forgotPassword(request):
    return render(request, 'login/forgotPassword.html')

def newUser(request):
    return render(request, 'login/newUser.html')