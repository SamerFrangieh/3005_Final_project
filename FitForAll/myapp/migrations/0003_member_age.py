# Generated by Django 5.0.3 on 2024-04-13 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_member_act_levels'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='age',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
    ]