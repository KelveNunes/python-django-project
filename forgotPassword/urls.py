from django.urls import path
from forgotPassword.views import forgotPassword

urlpatterns = [
    path('', forgotPassword)
]
