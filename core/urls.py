from .import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("partials/manage-resources/", views.manage_resources_partial, name="partial_manage_resources"),
    path("partials/manage-events/", views.manage_events_partial, name="partial_manage_events"),
    path("partials/notifications/", views.notifications_partial, name="partial_notifications"),
    path("partials/create_events_modal/", views.create_events_modal_partial, name="partial_create_events_modal"),
]