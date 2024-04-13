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
    print("Loading trainer dashboard...")  # Debugging line
    days_of_week = {
        '0': 'Sunday', '1': 'Monday', '2': 'Tuesday',
        '3': 'Wednesday', '4': 'Thursday', '5': 'Friday', '6': 'Saturday'
    }
    hours = list(range(24))  # Generate a list of hours from 0 to 23
    members = []

    trainer_id = request.session.get('trainer_id')
    print(f"Session Trainer ID: {trainer_id}")  # Debugging line
    if not trainer_id:
        return redirect('trainerLogin')

    trainer = Trainer.objects.filter(trainer_id=trainer_id).first()
    if not trainer:
        return redirect('trainerLogin')
    print(f"Trainer fetched: {trainer.name}")  # Debugging line

    # Fetch trainer availability and format it into structured keys
    availabilities = TrainerAvailability.objects.filter(trainer=trainer).order_by('day_of_week')
    structured_availabilities = {
        day: {
            'checked': False,
            'check_in': None,
            'check_out': None
        } for day in days_of_week.values()
    }

    for availability in availabilities:
        day_key = days_of_week[str(availability.day_of_week)]
        structured_availabilities[day_key]['checked'] = True
        structured_availabilities[day_key]['check_in'] = availability.check_in.strftime('%H:00')
        structured_availabilities[day_key]['check_out'] = availability.check_out.strftime('%H:00')
    print(f"Structured availabilities: {structured_availabilities}")  # Debugging line

    if request.method == 'POST':
        print(f"POST data received: {request.POST}")  # Debugging line
        if 'member_name' in request.POST:
            member_name = request.POST.get('member_name', '')
            members = Member.objects.filter(name__icontains=member_name)
        else:
            days_selected = request.POST.getlist('days')
            for day_value in days_of_week.keys():
                day_name = days_of_week[day_value]
                check_in_time = request.POST.get(f'check_in_{day_value}', None)
                check_out_time = request.POST.get(f'check_out_{day_value}', None)
                print(f"Processing day {day_name}: Selected - {day_value in days_selected}, Check-in: {check_in_time}, Check-out: {check_out_time}")  # Debugging line
                if day_value in days_selected and check_in_time and check_out_time:
                    TrainerAvailability.objects.update_or_create(
                        trainer=trainer,
                        day_of_week=int(day_value),
                        defaults={
                            'check_in': f"{check_in_time}:00",
                            'check_out': f"{check_out_time}:00"
                        }
                    )
                elif day_value not in days_selected:
                    TrainerAvailability.objects.filter(trainer=trainer, day_of_week=int(day_value)).delete()
                
            messages.success(request, 'Your availability has been updated successfully!')
            return redirect('trainerDashboard')

    context = {
        'days_of_week': days_of_week,
        'hours': hours,
        'members': members,
        'availabilities': structured_availabilities
    }
    return render(request, 'myapp/dashboard/trainerDashboard.html', context)

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




    if request.method == 'POST':
        member.diastolic_bp = request.POST.get('diastolic')
        member.systolic_bp = request.POST.get('systolic')
        if (member.diastolic_bp == '' or member.systolic_bp == ''):
            member.diastolic_bp =0
            member.systolic_bp = 0
        member.height = request.POST.get('Height')
        member.weight = request.POST.get('Weight')
        member.fitness_goal = request.POST.get('fitness_goals')
        member.act_levels = request.POST.get('act_levels')
        member.save()
        messages.success(request, "Profile updated successfully!")
    try:
        member.systolic_bp = int(member.systolic_bp)
    except ValueError:
        pass

    try:
        member.diastolic_bp = int(member.diastolic_bp)
    except ValueError:
        pass
    # Calculate BMI
    height_in_meters = float(member.height) / 100
    bmi = round(float(member.weight) / (height_in_meters ** 2), 1)
    bmi_category = ''
    if bmi < 19:
        bmi_category = 'Underweight 🟦'
    elif 19 <= bmi < 25:
        bmi_category = 'Healthy ✅'
    elif 25 <= bmi < 30:
        bmi_category = 'Overweight 🟨'
    elif 30 <= bmi < 40:
        bmi_category = 'Obese 🟧'
    else:
        bmi_category = 'Extremely Obese 🟥'

    # Calculate BMR
    bmr = 100
    rec_bmr = 100
    if member.age is None:
        member.age = 20
    bmr = int(round((88.362 + (13.397 * float(member.weight)) + (4.799 * float(member.height)) - (5.677 * float(member.age))),0))
    if member.act_levels == '1-3 x times a week':
        bmr = bmr + 800
    if member.act_levels == '3-5 x times a week':
        bmr = bmr + 1200
    if member.act_levels == '5-6 x times a week':
        bmr = bmr + 1600
    if member.act_levels == '6-7 x times a week':
        bmr = bmr + 1950

    rec_bmr = bmr

    if member.fitness_goal == 'lose_weight':
        rec_bmr = rec_bmr - 239
    
    if member.fitness_goal == 'gain_muscle':
        rec_bmr = rec_bmr + 226

    if member.fitness_goal == 'improve_endurance':
        rec_bmr = rec_bmr - 163

    if member.fitness_goal == 'increase_flexibility':
        rec_bmr = rec_bmr -121




    # Calculate BP rating
    bp_health = ''
    bp = str(member.systolic_bp) + '/' + str(member.diastolic_bp)
    if member.systolic_bp >= 180 or member.diastolic_bp >= 120:
        bp_health = 'High: Stage 2 Hypertension'
    elif 160 <= member.systolic_bp < 180 or 100 <= member.diastolic_bp < 110:
        bp_health = 'High: Stage 1 Hypertension'
    elif 140 <= member.systolic_bp < 160 or 90 <= member.diastolic_bp < 100:
        bp_health = 'Prehypertension'
    elif 120 <= member.systolic_bp < 140 and member.diastolic_bp < 90:
        bp_health = 'Normal'
    elif member.systolic_bp < 120 and member.diastolic_bp < 80:
        bp_health = 'Low'
    else:
        bp_health = 'Consult a doctor'



    if request.method == 'POST':
        member.diastolic_bp = request.POST.get('diastolic')
        member.systolic_bp = request.POST.get('systolic')
        member.height = request.POST.get('Height')
        member.weight = request.POST.get('Weight')
        member.fitness_goal = request.POST.get('fitness_goals')
        member.act_levels = request.POST.get('act_levels')
        member.age = request.POST.get('Age')
        member.save()
        messages.success(request, "Profile updated successfully!")
        context = {'member': member, 'bmi': bmi, 'bmi_category': bmi_category, 'bp_health': bp_health, 'bp': bp, 'bmr': bmr,'rec_bmr': rec_bmr}
        return render(request, 'myapp/dashboard/index.html', context)

    context = {'member': member, 'bmi': bmi, 'bmi_category': bmi_category, 'bp_health': bp_health, 'bp': bp, 'bmr': bmr,'rec_bmr': rec_bmr}
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
    

