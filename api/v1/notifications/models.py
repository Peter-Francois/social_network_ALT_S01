from django.db import models
from api.v1.users.models import User


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('event_update', 'Event Update'),
        ('event_reminder', 'Event Reminder'),
        ('rsvp_update', 'RSVP Update'),
        ('resource_shared', 'Resource Shared'),

    ]

    PRIORITY_LEVELS = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    title = models.CharField(max_length=255)
    content = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_LEVELS, default='medium')
    read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    action_url = models.TextField(blank=True, null=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_notifications')
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='sent_notifications')
    relation_id = models.PositiveIntegerField(null=True, blank=True)
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['recipient', 'read', 'created_at'], name='idx_user_notifications'),
            models.Index(fields=['type'], name='idx_notification_type'),
        ]
        db_table = 'Notifications'

    def __str__(self):
        return f"{self.type.title()} notification for {self.recipient}"