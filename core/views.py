
from django.shortcuts import render


def dashboard(request):
    return render(request, 'core/dashboard.html')


def projects(request):
    return render(request, 'core/projects.html')


def tasks(request):
    return render(request, 'core/tasks.html')


def issues(request):
    return render(request, 'core/issues.html')
