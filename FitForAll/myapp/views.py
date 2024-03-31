from django.shortcuts import render
from django.http import HttpResponse

#from .models import Book
def member_login(request):
    return render(request, 'myapp/login/memberLogin.html')

def dashboard_view(request):
    # Will put objects here once Samer creates dashboard frontend
    # objects = YourModel.objects.all()

    # Dashboard no context
    return render(request, 'myapp/dashboard/index.html')

def register(request):
    return render(request, 'myapp/registration/register.html')
def train_login(request):
    return render(request, 'myapp/login/trainerLogin.html')

def admin_login(request):
    return render(request, 'myapp/login/adminLogin.html')
def member_login(request):
    return render(request, 'myapp/login/memberLogin.html')
