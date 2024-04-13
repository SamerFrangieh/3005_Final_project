from django.db import models
from django.contrib.postgres.fields import JSONField
# for Equipment
from django.utils import timezone



class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # Consider using Django's built-in User model for better security
    health_metrics = models.JSONField()
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Allow null if optional
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Allow null if optional
    goal_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weeks_to_goal = models.IntegerField(null=True, blank=True)
    diastolic_bp = models.IntegerField(verbose_name="Diastolic Blood Pressure",null=True, default=0)
    systolic_bp = models.IntegerField(verbose_name="Systolic Blood Pressure",null=True, default=0)
    fitness_goal = models.CharField(max_length=255, blank=True, null=True,verbose_name="Fitness Goal")
    act_levels = models.CharField(max_length=255, blank=True, null=True,verbose_name="Activity Levels",default="1-3 x times a week")
    age = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True,default=20)  # Allow null if optional

class Trainer(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255) 


class TrainerAvailability(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='availabilities')
    day_of_week = models.IntegerField(choices=[
        (0, 'Sunday'),
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
    ])
    check_in = models.TimeField()
    check_out = models.TimeField()

    def __str__(self):
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return f"{self.trainer.name} - {days[self.day_of_week]}"
class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255) 


class PersonalSession(models.Model):
    personal_session_id = models.AutoField(primary_key=True)
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name='personal_sessions'
    )
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='personal_sessions'
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Room {self.room_id} - {self.name}"

class GroupFitnessClass(models.Model):
    group_fitness_class_id = models.AutoField(primary_key=True)
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.CASCADE,
        related_name='group_fitness_classes'
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='group_fitness_classes'
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class MemberGroupFitnessRegistration(models.Model):
    # Foreign key to the GroupFitnessClass model
    group_fitness_class = models.ForeignKey(
        'GroupFitnessClass',
        on_delete=models.CASCADE,
        related_name='registrations'
    )
    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name='group_fitness_registrations'
    )
    registration_date = models.DateField(auto_now_add=True)

class EquipmentMaintenance(models.Model):
    # Status choices
    IN_MAINTENANCE = 'IN_MAINTENANCE'
    BROKEN = 'BROKEN'
    FUNCTIONING = 'FUNCTIONING'
    STATUS_CHOICES = [
        (IN_MAINTENANCE, 'In Maintenance'),
        (BROKEN, 'Broken'),
        (FUNCTIONING, 'Functioning'),
    ]

    equipment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    last_maintenance_date = models.DateField()
    next_maintenance_date = models.DateField()
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=FUNCTIONING,
    )

