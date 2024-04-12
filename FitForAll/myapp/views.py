from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db import connection
 # Prints the last executed query
# #from .models import Book
# def member_login(request):
#     return render(request, 'myapp/login/memberLogin.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Member

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        password = request.POST.get('password').strip()
        fitness_goals = request.POST.get('goals', '').strip() # Optional, provide default
        height = request.POST.get('height').strip()
        weight = request.POST.get('weight').strip()

        # Basic validation (you might want to add more, e.g., checking if user already exists)
        if not (name and password and height and weight):
            messages.error(request, "Please fill out all required fields.")
            return render(request, 'myapp/registration/register.html')

        try:
            # Assuming height and weight are stored as DecimalFields in your model
            member = Member.objects.create(
                name=name,
                password=password,  # For demonstration; in real applications, use Django's user model & hash passwords
                fitness_goal=fitness_goals,
                height=height,
                weight=weight,
                health_metrics={}  # Assuming you have a default or an empty value for starters
            )
            # Redirect to login page or dashboard after successful registration
            return render(request, 'myapp/login/memberLogin.html')  # Assuming you have a URL named 'memberLogin'
        except Exception as e:
            messages.error(request, "An error occurred during registration. Please try again.")
            print(e)  # or use logging
            return render(request, 'myapp/registration/register.html')
    else:
        return render(request, 'myapp/registration/register.html')

def train_login(request):
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        password = request.POST.get('password').strip()

        # Assuming at least this query will be made
        try:
            trainer = Trainer.objects.get(name=name, password=password)
            # Print the last query, safely inside a conditional block ensuring at least one query was made
            print(connection.queries[-1])  # Safer usage
        except Trainer.DoesNotExist:
            # Print the last query, safely inside a conditional block ensuring at least one query was made
            print(connection.queries[-1])  # Safer usage
            return render(request, 'myapp/login/trainerLogin.html', {'error': 'Invalid username or password'})
        
        # Print the last query, safely inside a conditional block ensuring at least one query was made
        print(connection.queries[-1])  # Safer usage
        
        request.session['trainer_id'] = trainer.trainer_id
        return redirect('trainerDashboard')
    else:
        return render(request, 'myapp/login/trainerLogin.html')

def admin_login(request):
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        password = request.POST.get('password').strip()

        # Assuming at least this query will be made
        try:
            admin = Admin.objects.get(name=name, password=password)
            # Print the last query, safely inside a conditional block ensuring at least one query was made
            print(connection.queries[-1])  # Safer usage
        except Admin.DoesNotExist:
            # Print the last query, safely inside a conditional block ensuring at least one query was made
            print(connection.queries[-1])  # Safer usage
            return render(request, 'myapp/login/adminLogin.html', {'error': 'Invalid username or password'})
        
        # Print the last query, safely inside a conditional block ensuring at least one query was made
        print(connection.queries[-1])  # Safer usage
        
        request.session['admin_id'] = admin.admin_id
        return redirect('adminDashboard')
    else:
        return render(request, 'myapp/login/adminLogin.html')
    

def trainerDashboard(request):
    return render(request, 'myapp/dashboard/trainerDashboard.html')
def adminDashboard(request):
    return render(request, 'myapp/dashboard/adminDashboard.html')

def dashboard(request):
    if not request.session.get('member_id'):
        return redirect('memberLogin')

    member_id = request.session['member_id']
    try:
        member = Member.objects.get(member_id=member_id)
    except Member.DoesNotExist:
        return redirect('memberLogin')  # Consider adding an error message or similar

    # Calculate BMI
    height_in_meters = float(member.height) / 100
    bmi = round(float(member.weight) / (height_in_meters ** 2), 1)
    bmi_category = ''
    if bmi < 19:
        bmi_category = 'Underweight'
    elif 19 <= bmi < 25:
        bmi_category = 'Healthy'
    elif 25 <= bmi < 30:
        bmi_category = 'Overweight'
    elif 30 <= bmi < 40:
        bmi_category = 'Obese'
    else:
        bmi_category = 'Extremely Obese'


    if request.method == 'POST':
        member.diastolic_bp = request.POST.get('diastolic')
        member.systolic_bp = request.POST.get('systolic')
        member.height = request.POST.get('Height')
        member.weight = request.POST.get('Weight')
        member.fitness_goal = request.POST.get('fitness_goals')
        member.save()
        messages.success(request, "Profile updated successfully!")
        context = {'member': member, 'bmi': bmi, 'bmi_category': bmi_category}
        return render(request, 'myapp/dashboard/index.html', context)

    context = {'member': member, 'bmi': bmi, 'bmi_category': bmi_category}
    return render(request, 'myapp/dashboard/index.html', context)


def member_login(request):
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        password = request.POST.get('password').strip()

        # Assuming at least this query will be made
        try:
            member = Member.objects.get(name=name, password=password)
            # Print the last query, safely inside a conditional block ensuring at least one query was made
        except Member.DoesNotExist:
            # Print the last query, safely inside a conditional block ensuring at least one query was made
            return render(request, 'myapp/login/memberLogin.html', {'error': 'Invalid username or password'})
        
        
        request.session['member_id'] = member.member_id
        return redirect('dashboard')
    else:
        return render(request, 'myapp/login/memberLogin.html')
    

