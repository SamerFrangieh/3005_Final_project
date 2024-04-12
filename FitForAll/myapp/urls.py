from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_login, name='memberLogin'),  # This is where you define the URL name.
    path('dashboard/index.html', views.dashboard, name='dashboard'),
    path('dashboard/trainerDashboard.html', views.trainerDashboard, name='trainerDashboard'),
    path('dashboard/adminDashboard.html', views.adminDashboard, name='adminDashboard'),
    path('registration/register.html', views.register, name='register'),
    path('login/memberLogin.html', views.member_login, name='memberLogin'),
    path('login/adminLogin.html', views.admin_login, name='adminLogin'),
    path('login/trainerLogin.html', views.train_login, name='trainerLogin')

]
