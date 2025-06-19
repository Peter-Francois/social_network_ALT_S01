from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {
        "initial_partial": "partials/manage_resources.html"
    })

def manage_resources_partial(request):
    return render(request, 'partials/manage_resources.html')

def manage_events_partial(request):
    return render(request, 'partials/manage_events.html')

def notifications_partial(request):
    return render(request, 'partials/notifications.html')
