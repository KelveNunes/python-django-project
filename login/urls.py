from django.urls import path
from login.views import login,forgotPassword, newUser

urlpatterns = [
    path('', login),
    path('forgotPassword/', forgotPassword, name='forgot-password'),
    path('newUser/', newUser, name='new-user'),
]
