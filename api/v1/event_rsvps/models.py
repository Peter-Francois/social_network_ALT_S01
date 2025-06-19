from django.db import models
from api.v1.events.models import Event
from api.v1.users.models import User

class EventRSVP(models.Model):
    STATUS_CHOICES = [
        ('attending', 'Attending'),
        ('declined', 'Declined'),
        ('maybe', 'Maybe'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    response_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rsvps')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rsvps')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('event', 'user')
        indexes = [
            models.Index(fields=['user', 'status'], name='idx_user_rsvps'),
        ]
        db_table = 'EventRSVPs'

    def __str__(self):
        return f"{self.user} RSVP for {self.event}: {self.status}"