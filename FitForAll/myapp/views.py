from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.db import connection
import os
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

    context = {}


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
        member.age = request.POST.get('Age')
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

    #The workout schedules

    mon = ""
    tue = ''
    wed = ''
    thu = ''
    fri = ''
    sat = ''
    sun = ''

    if member.fitness_goal == 'gain_muscle':
        
        if member.act_levels == '1-3 x times a week':
            mon= 'Day 1: Push (Chest, Shoulders, and Triceps)//Bench Press - 4 sets of 8-12 reps,\n//Overhead Press - 3 sets of 8-12 reps,\n//Incline Dumbbell Press - 3 sets of 8-12 reps,\n//Lateral Raises - 3 sets of 12-15 reps,\n//Tricep Dips - 3 sets of 10-15 reps,//Tricep Pushdowns - 3 sets of 10-15 reps\n'
            tue = 'rest'
            wed = 'Day 2: Pull (Back, Biceps)//Deadlifts - 3 sets of 6-8 reps//Pull-ups - 3 sets of as many reps as possible//Barbell Rows - 3 sets of 8-12 reps//Face Pulls - 3 sets of 12-15 reps//Hammer Curls - 3 sets of 10-12 reps//Barbell Curls - 3 sets of 8-12 reps'
            thu = 'rest'
            fri = "Day 3: Legs (Quads, Hamstrings, and Calves)//Squats - 4 sets of 8-12 reps//Leg Press - 3 sets of 10-12 reps//Romanian Deadlifts - 3 sets of 8-12 reps//Leg Curls - 3 sets of 10-12 reps//Calf Raises - 5 sets of 12-15 reps"
            sat = 'rest'
            sun = 'rest'
        elif member.act_levels == '3-5 x times a week':
            mon= 'Day 1: Push (Chest, Shoulders, and Triceps)//Bench Press - 4 sets of 8-12 reps,\n//Overhead Press - 3 sets of 8-12 reps,\n//Incline Dumbbell Press - 3 sets of 8-12 reps,\n//Lateral Raises - 3 sets of 12-15 reps,\n//Tricep Dips - 3 sets of 10-15 reps,//Tricep Pushdowns - 3 sets of 10-15 reps\n'
            tue = 'rest'
            wed = 'Day 2: Pull (Back, Biceps)//Deadlifts - 3 sets of 6-8 reps//Pull-ups - 3 sets of as many reps as possible//Barbell Rows - 3 sets of 8-12 reps//Face Pulls - 3 sets of 12-15 reps//Hammer Curls - 3 sets of 10-12 reps//Barbell Curls - 3 sets of 8-12 reps'
            thu = 'Day 3: Arm Workout Day: Biceps and Triceps//Barbell Curl - 4 sets of 8-12 reps//Tricep Dips - 4 sets of 8-12 reps//Hammer Curls - 3 sets of 10-12 reps//Skull Crushers - 3 sets of 8-12 reps//Preacher Curl - 3 sets of 8-12 reps'
            fri = "Day 4: Legs (Quads, Hamstrings, and Calves)//Squats - 4 sets of 8-12 reps//Leg Press - 3 sets of 10-12 reps//Romanian Deadlifts - 3 sets of 8-12 reps//Leg Curls - 3 sets of 10-12 reps//Calf Raises - 5 sets of 12-15 reps"
            sat = 'rest'
            sun = 'rest'
        elif member.act_levels == '5-6 x times a week':
            mon= 'Day 1: Push (Chest, Shoulders, and Triceps)//Bench Press - 4 sets of 8-12 reps,\n//Overhead Press - 3 sets of 8-12 reps,\n//Incline Dumbbell Press - 3 sets of 8-12 reps,\n//Lateral Raises - 3 sets of 12-15 reps,\n//Tricep Dips - 3 sets of 10-15 reps,//Tricep Pushdowns - 3 sets of 10-15 reps\n'
            tue = 'Day 2: Pull (Back, Biceps)//Deadlifts - 3 sets of 6-8 reps//Pull-ups - 3 sets of as many reps as possible//Barbell Rows - 3 sets of 8-12 reps//Face Pulls - 3 sets of 12-15 reps//Hammer Curls - 3 sets of 10-12 reps//Barbell Curls - 3 sets of 8-12 reps'
            wed = "Day 3: Legs (Quads, Hamstrings, and Calves)//Squats - 4 sets of 8-12 reps//Leg Press - 3 sets of 10-12 reps//Romanian Deadlifts - 3 sets of 8-12 reps//Leg Curls - 3 sets of 10-12 reps//Calf Raises - 5 sets of 12-15 reps"
            thu = 'Day 4: Push (Chest, Shoulders, and Triceps)//Bench Press - 4 sets of 8-12 reps,\n//Overhead Press - 3 sets of 8-12 reps,\n//Incline Dumbbell Press - 3 sets of 8-12 reps,\n//Lateral Raises - 3 sets of 12-15 reps,\n//Tricep Dips - 3 sets of 10-15 reps,//Tricep Pushdowns - 3 sets of 10-15 reps\n'
            fri = 'Day 5: Pull (Back, Biceps)//Deadlifts - 3 sets of 6-8 reps//Pull-ups - 3 sets of as many reps as possible//Barbell Rows - 3 sets of 8-12 reps//Face Pulls - 3 sets of 12-15 reps//Hammer Curls - 3 sets of 10-12 reps//Barbell Curls - 3 sets of 8-12 reps'
            sat = "Day 6: Legs (Quads, Hamstrings, and Calves)//Squats - 4 sets of 8-12 reps//Leg Press - 3 sets of 10-12 reps//Romanian Deadlifts - 3 sets of 8-12 reps//Leg Curls - 3 sets of 10-12 reps//Calf Raises - 5 sets of 12-15 reps"
            sun = 'rest'
        elif member.act_levels =='6-7 x times a week':
            mon= 'Day 1: Push (Chest, Shoulders, and Triceps)//Bench Press - 4 sets of 8-12 reps,\n//Overhead Press - 3 sets of 8-12 reps,\n//Incline Dumbbell Press - 3 sets of 8-12 reps,\n//Lateral Raises - 3 sets of 12-15 reps,\n//Tricep Dips - 3 sets of 10-15 reps,//Tricep Pushdowns - 3 sets of 10-15 reps\n'
            tue = 'Day 2: Pull (Back, Biceps)//Deadlifts - 3 sets of 6-8 reps//Pull-ups - 3 sets of as many reps as possible//Barbell Rows - 3 sets of 8-12 reps//Face Pulls - 3 sets of 12-15 reps//Hammer Curls - 3 sets of 10-12 reps//Barbell Curls - 3 sets of 8-12 reps'
            wed = "Day 3: Legs (Quads, Hamstrings, and Calves)//Squats - 4 sets of 8-12 reps//Leg Press - 3 sets of 10-12 reps//Romanian Deadlifts - 3 sets of 8-12 reps//Leg Curls - 3 sets of 10-12 reps//Calf Raises - 5 sets of 12-15 reps"
            thu = 'Day 4: Push (Chest, Shoulders, and Triceps)//Bench Press - 4 sets of 8-12 reps,\n//Overhead Press - 3 sets of 8-12 reps,\n//Incline Dumbbell Press - 3 sets of 8-12 reps,\n//Lateral Raises - 3 sets of 12-15 reps,\n//Tricep Dips - 3 sets of 10-15 reps,//Tricep Pushdowns - 3 sets of 10-15 reps\n'
            fri = 'Day 5: Pull (Back, Biceps)//Deadlifts - 3 sets of 6-8 reps//Pull-ups - 3 sets of as many reps as possible//Barbell Rows - 3 sets of 8-12 reps//Face Pulls - 3 sets of 12-15 reps//Hammer Curls - 3 sets of 10-12 reps//Barbell Curls - 3 sets of 8-12 reps'
            sat = "Day 6: Legs (Quads, Hamstrings, and Calves)//Squats - 4 sets of 8-12 reps//Leg Press - 3 sets of 10-12 reps//Romanian Deadlifts - 3 sets of 8-12 reps//Leg Curls - 3 sets of 10-12 reps//Calf Raises - 5 sets of 12-15 reps"
            sun = 'Day 7: Arm Workout Day: Biceps and Triceps//Barbell Curl - 4 sets of 8-12 reps//Tricep Dips - 4 sets of 8-12 reps//Hammer Curls - 3 sets of 10-12 reps//Skull Crushers - 3 sets of 8-12 reps//Preacher Curl - 3 sets of 8-12 reps'
        
    elif member.fitness_goal == 'lose_weight':
        if member.act_levels == '1-3 x times a week':
            mon= 'Day 1: Cardio and Core//Treadmill Running - 30 minutes at a moderate pace//Cycling - 20 minutes at a vigorous pace//Russian Twists - 4 sets of 15 reps each side//Leg Raises - 4 sets of 12 reps'
            tue = 'rest'
            wed = 'Day 2: Full Body Strength//Squats - 4 sets of 10-12 reps//Bench Press - 4 sets of 10-12 reps//Deadlifts - 3 sets of 10 reps//Pull-ups - 3 sets of AMRAP//Plank - 3 sets of 1 min hold'
            thu = 'rest'
            fri = "Day 3: High-Intensity Interval Training (HIIT)//Sprints - 10 rounds of 30 seconds sprint/30 seconds rest//Burpees - 5 sets of 20 seconds on/40 seconds rest//Jump Rope - 10 minutes with intervals of 1 minute on/1 minute off"
            sat = 'rest'
            sun = 'rest'
        elif member.act_levels == '3-5 x times a week':
            mon= 'Day 1: Cardio and Core//Treadmill Running - 30 minutes at a moderate pace//Cycling - 20 minutes at a vigorous pace//Russian Twists - 4 sets of 15 reps each side//Leg Raises - 4 sets of 12 reps'
            tue = 'rest'
            wed = 'Day 2: Full Body Strength//Squats - 4 sets of 10-12 reps//Bench Press - 4 sets of 10-12 reps//Deadlifts - 3 sets of 10 reps//Pull-ups - 3 sets of AMRAP//Plank - 3 sets of 1 min hold'
            thu = 'rest'
            fri = "Day 3: High-Intensity Interval Training (HIIT)//Sprints - 10 rounds of 30 seconds sprint/30 seconds rest//Burpees - 5 sets of 20 seconds on/40 seconds rest//Jump Rope - 10 minutes with intervals of 1 minute on/1 minute off"
            sat = 'Day 4: Full Body Strength//Squats - 4 sets of 10-12 reps//Bench Press - 4 sets of 10-12 reps//Deadlifts - 3 sets of 10 reps//Pull-ups - 3 sets of AMRAP//Plank - 3 sets of 1 min hold'
            sun = 'rest'
        elif member.act_levels == '5-6 x times a week':
            mon= 'Day 1: Cardio and Core//Treadmill Running - 30 minutes at a moderate pace//Cycling - 20 minutes at a vigorous pace//Russian Twists - 4 sets of 15 reps each side//Leg Raises - 4 sets of 12 reps'
            tue = 'Day 2: Full Body Strength//Squats - 4 sets of 10-12 reps//Bench Press - 4 sets of 10-12 reps//Deadlifts - 3 sets of 10 reps//Pull-ups - 3 sets of AMRAP//Plank - 3 sets of 1 min hold'
            wed = 'Day 3: Full Body Strength//Squats - 4 sets of 10-12 reps//Bench Press - 4 sets of 10-12 reps//Deadlifts - 3 sets of 10 reps//Pull-ups - 3 sets of AMRAP//Plank - 3 sets of 1 min hold'
            thu = 'rest'
            fri = "Day 4: High-Intensity Interval Training (HIIT)//Sprints - 10 rounds of 30 seconds sprint/30 seconds rest//Burpees - 5 sets of 20 seconds on/40 seconds rest//Jump Rope - 10 minutes with intervals of 1 minute on/1 minute off"
            sat = 'Day 5: Full Body Strength//Squats - 4 sets of 10-12 reps//Bench Press - 4 sets of 10-12 reps//Deadlifts - 3 sets of 10 reps//Pull-ups - 3 sets of AMRAP//Plank - 3 sets of 1 min hold'
            sun = 'rest'
        elif member.act_levels =='6-7 x times a week':
            mon= 'Day 1: Cardio and Core//Treadmill Running - 30 minutes at a moderate pace//Cycling - 20 minutes at a vigorous pace//Russian Twists - 4 sets of 15 reps each side//Leg Raises - 4 sets of 12 reps'
            tue = 'Day 2: Full Body Strength//Squats - 4 sets of 10-12 reps//Bench Press - 4 sets of 10-12 reps//Deadlifts - 3 sets of 10 reps//Pull-ups - 3 sets of AMRAP//Plank - 3 sets of 1 min hold'
            wed = 'Day 3: Full Body Strength//Squats - 4 sets of 10-12 reps//Bench Press - 4 sets of 10-12 reps//Deadlifts - 3 sets of 10 reps//Pull-ups - 3 sets of AMRAP//Plank - 3 sets of 1 min hold'
            thu = 'Day 6: Active RecoveryYoga - 60 minutes focusing on flexibility and core//Light Walking - 30 minutes at a gentle pace'
            fri = "Day 4: High-Intensity Interval Training (HIIT)//Sprints - 10 rounds of 30 seconds sprint/30 seconds rest//Burpees - 5 sets of 20 seconds on/40 seconds rest//Jump Rope - 10 minutes with intervals of 1 minute on/1 minute off"
            sat = 'Day 5: Full Body Strength//Squats - 4 sets of 10-12 reps//Bench Press - 4 sets of 10-12 reps//Deadlifts - 3 sets of 10 reps//Pull-ups - 3 sets of AMRAP//Plank - 3 sets of 1 min hold'
            sun = 'rest'

    elif member.fitness_goal == 'improve_endurance':
        if member.act_levels == '1-3 x times a week':
            mon = "Day 1: Cardio Intervals//Treadmill or Outdoor Running - 30 minutes of interval training (1 min fast/2 min slow)"
            tue = "rest"
            wed = "Day 2: Full Body Circuit//Bodyweight Exercises (Push-ups, Pull-ups, Squats) - 3 rounds of 15 reps each"
            thu = "rest"
            fri = "Day 3: Long Duration Cardio//Cycling or Swimming - 45 minutes at a steady pace"
            sat = "rest"
            sun = "rest"

        elif member.act_levels == '3-5 x times a week':
            mon = "Day 1: High Intensity Interval Training//HIIT - 20 minutes (30s high intensity/30s low intensity)"
            tue = "rest"
            wed = "Day 2: Strength and Endurance Circuit//Mix of Weight Lifting and Bodyweight Exercises - 3 sets of 12 reps"
            thu = "Day 3: Cardio Intervals//Rowing Machine or Jump Rope - 20 minutes of interval training"
            fri = "rest"
            sat = "Day 4: Long Duration Cardio//Jogging - 60 minutes at a moderate pace"
            sun = "rest"

        elif member.act_levels == '5-6 x times a week':
            mon = "Day 1: Cardio Intervals//Treadmill Sprints - 30 minutes of interval training (1 min sprint/2 min walk)"
            tue = "Day 2: Circuit Training//Full body circuit with resistance bands - 3 circuits of 10 mins each"
            wed = "rest"
            thu = "Day 3: Strength Training//Bodyweight strength exercises - 4 sets of 10-12 reps"
            fri = "Day 4: Cardio Endurance//Steady State Cycling - 50 minutes at a moderate intensity"
            sat = "Day 5: Active Recovery//Yoga or light stretching - 30 minutes"
            sun = "rest"

        elif member.act_levels == '6-7 x times a week':
            mon = "Day 1: Interval Training//Treadmill intervals - 25 minutes (3 min run/2 min walk)"
            tue = "Day 2: Circuit Training//Kettlebell circuit - 4 sets of 15 reps"
            wed = "Day 3: Endurance Cardio//Long distance running - 60 minutes at a steady pace"
            thu = "Day 4: High-Intensity Bodyweight//Tabata style - 20 minutes (20s work/10s rest)"
            fri = "Day 5: Strength Focus//Compound lifting - Squats, Deadlifts, Bench Press - 3 sets of 8-12 reps"
            sat = "Day 6: Mixed Cardio//Rowing and Cycling - 45 minutes total"
            sun = "Day 7: Active Rest//Stretching and foam rolling - 30 minutes"

    if member.fitness_goal == 'increase_flexibility':
        if member.act_levels == '1-3 x times a week':
            mon = "Day 1: Yoga Stretching//Full body yoga - 30 minutes"
            tue = "rest"
            wed = "Day 2: Dynamic Stretching//Full body dynamic stretches - 20 minutes"
            thu = "rest"
            fri = "Day 3: Pilates//Beginner Pilates session - 30 minutes"
            sat = "rest"
            sun = "rest"

        elif member.act_levels == '3-5 x times a week':
            mon = "Day 1: Yoga Stretching//Full body yoga - 45 minutes"
            tue = "rest"
            wed = "Day 2: Dynamic Stretching//Leg and hip dynamic stretches - 20 minutes"
            thu = "Day 3: Tai Chi//Beginner Tai Chi class - 30 minutes"
            fri = "rest"
            sat = "Day 4: Pilates//Intermediate Pilates session - 40 minutes"
            sun = "rest"

        elif member.act_levels == '5-6 x times a week':
            mon = "Day 1: Yoga Stretching//Advanced yoga poses - 45 minutes"
            tue = "Day 2: Pilates//Core-focused Pilates - 40 minutes"
            wed = "rest"
            thu = "Day 3: Dynamic Stretching//Full body dynamic stretches - 30 minutes"
            fri = "Day 4: Tai Chi//Intermediate Tai Chi session - 45 minutes"
            sat = "Day 5: Active Recovery//Light yoga and meditation - 30 minutes"
            sun = "rest"

        elif member.act_levels == '6-7 x times a week':
            mon = "Day 1: Yoga Stretching//Intensive yoga session - 60 minutes"
            tue = "Day 2: Dynamic Stretching//Sports specific stretches - 30 minutes"
            wed = "Day 3: Pilates//Advanced Pilates session - 45 minutes"
            thu = "Day 4: Yoga Stretching//Power yoga - 45 minutes"
            fri = "Day 5: Tai Chi//Advanced Tai Chi practice - 60 minutes"
            sat = "Day 6: Dynamic Stretching//Injury prevention stretches - 30 minutes"
            sun = "Day 7: Active Rest//Gentle yoga and deep breathing - 30 minutes"



    context['member'] = member
    context['bmi'] = bmi
    context['bmi_category'] = bmi_category
    context['bp_health'] = bp_health
    context['bp'] = bp
    context['bmr'] = bmr
    context['rec_bmr'] = rec_bmr
    context['mon'] = mon
    context['tue'] = tue
    context['wed'] = wed
    context['thu'] = thu
    context['fri'] = fri
    context['sat'] = sat
    context['sun'] = sun

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
    

