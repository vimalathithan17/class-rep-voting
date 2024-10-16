from django.urls import path
from . import views
from django_otp.forms import OTPAuthenticationForm
from django_otp.views import LoginView
app_name = 'homepage'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/',LoginView.as_view(template_name='homepage/otp.html'),name='login'),
    
]
