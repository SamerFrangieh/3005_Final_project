# Generated by Django 5.0.3 on 2024-04-13 02:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentMaintenance',
            fields=[
                ('equipment_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('last_maintenance_date', models.DateField()),
                ('next_maintenance_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupFitnessClass',
            fields=[
                ('group_fitness_class_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('health_metrics', models.JSONField()),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('goal_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('weeks_to_goal', models.IntegerField(blank=True, null=True)),
                ('diastolic_bp', models.IntegerField(default=0, null=True, verbose_name='Diastolic Blood Pressure')),
                ('systolic_bp', models.IntegerField(default=0, null=True, verbose_name='Systolic Blood Pressure')),
                ('fitness_goal', models.CharField(blank=True, max_length=255, null=True, verbose_name='Fitness Goal')),
                ('act_levels', models.CharField(blank=True, default='1-3 x times a week', max_length=255, null=True, verbose_name='Activity Levels')),
                ('age', models.DecimalField(blank=True, decimal_places=0, default=20, max_digits=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('trainer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.member')),
            ],
        ),
        migrations.CreateModel(
            name='MemberGroupFitnessRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('group_fitness_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='myapp.groupfitnessclass')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_fitness_registrations', to='myapp.member')),
            ],
        ),
        migrations.AddField(
            model_name='groupfitnessclass',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_fitness_classes', to='myapp.room'),
        ),
        migrations.CreateModel(
            name='PersonalSession',
            fields=[
                ('personal_session_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personal_sessions', to='myapp.member')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personal_sessions', to='myapp.trainer')),
            ],
        ),
        migrations.AddField(
            model_name='groupfitnessclass',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_fitness_classes', to='myapp.trainer'),
        ),
        migrations.CreateModel(
            name='TrainerAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.IntegerField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')])),
                ('check_in', models.TimeField()),
                ('check_out', models.TimeField()),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='myapp.trainer')),
            ],
        ),
    ]
