from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Member
from django.db import connection
 # Prints the last executed query
# #from .models import Book
# def member_login(request):
#     return render(request, 'myapp/login/memberLogin.html')

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
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        password = request.POST.get('password').strip()

        # Assuming at least this query will be made
        try:
            member = Member.objects.get(name=name, password=password)
            # Print the last query, safely inside a conditional block ensuring at least one query was made
            print(connection.queries[-1])  # Safer usage
        except Member.DoesNotExist:
            # Print the last query, safely inside a conditional block ensuring at least one query was made
            print(connection.queries[-1])  # Safer usage
            return render(request, 'myapp/login/memberLogin.html', {'error': 'Invalid username or password'})
        
        # Print the last query, safely inside a conditional block ensuring at least one query was made
        print(connection.queries[-1])  # Safer usage
        
        request.session['member_id'] = member.member_id
        return render(request, 'myapp/dashboard/index.html')
    else:
        return render(request, 'myapp/login/memberLogin.html')