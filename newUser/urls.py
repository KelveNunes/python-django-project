from django.urls import path
from newUser.views import newUser

urlpatterns = [
    path('', newUser)
]
