from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_login, name='memberLogin'),
    path('dashboard/index.html', views.dashboard_view, name='dashboard')
    
]
