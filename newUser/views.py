from django.shortcuts import render

def newUser(request):
    return render(request, 'newUser/newUser.html')