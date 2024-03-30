from django.shortcuts import render

#from .models import Book

def dashboard_view(request):
    # Will put objects here once Samer creates dashboard frontend
    # objects = YourModel.objects.all()

    # Dashboard no context
    return render(request, 'myapp/dashboard/index.html')