from django.shortcuts import render


def forgotPassword(request):
    return render(request, 'forgotPassword/forgotPassword.html')