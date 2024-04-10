from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

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



def member_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and not user.is_staff:
            login(request, user)
            # Redirect to member dashboard or any other member page
            return redirect('myapp/dashboard/index.html')  # Assuming 'dashboard' is the name of your member dashboard URL
        else:
            return render(request, 'myapp/login/memberLogin.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'myapp/login/memberLogin.html')
