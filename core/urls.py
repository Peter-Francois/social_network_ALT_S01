from .import views
from django.urls import path

urlpatterns = [
    path('', views.manage_resources, name='index'),
    path('manage_resources/', views.manage_resources, name='manage_resources'),
    path('manage_events/', views.manage_events, name='manage_events'),
    path('notifications/', views.notifications, name='notifications'),
]