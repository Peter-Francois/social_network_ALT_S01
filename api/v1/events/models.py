from django.db import models
from api.v1.users.models import User
from api.v1.user_groups.models import UserGroup


class Event(models.Model):
    LOCATION_TYPE_CHOICES = [
        ('virtual', 'Virtual'),
        ('physical', 'Physical'),
        ('hybrid', 'Hybrid'),
    ]

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('cancelled', 'Cancelled'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    location_type = models.CharField(max_length=50, choices=LOCATION_TYPE_CHOICES, blank=True, null=True)
    max_participants = models.IntegerField(blank=True, null=True)
    is_private = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    group = models.ForeignKey(UserGroup, on_delete=models.SET_NULL, null=True, blank=True, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['start_date', 'end_date'], name='idx_event_dates'),
            models.Index(fields=['status'], name='idx_event_status'),
        ]

    def __str__(self):
        return self.title