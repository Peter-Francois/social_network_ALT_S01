from django.shortcuts import render
from django.http import HttpResponse


def manage_resources(request):
    return render(request, 'core/manage_resources.html')

def manage_events(request):
    return render(request, 'core/manage_events.html')

def notifications(request):
    return render(request, 'core/notifications.html')
