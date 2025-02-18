from django.urls import path
from login.views import login,forgotPassword, newUser

urlpatterns = [
    path('', login),
    path('forgotPassword/', forgotPassword),
    path('newUser/', newUser),
]
