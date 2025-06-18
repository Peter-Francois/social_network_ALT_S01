from django.db import models
from api.v1.events.models import Event
from api.v1.shared_resources.models import SharedResource

class EventResource(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='resources')
    resource = models.ForeignKey(SharedResource, on_delete=models.CASCADE, related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('event', 'resource')
        db_table = 'EventResources'

    def __str__(self):
        return f"Resource '{self.resource}' linked to Event '{self.event}'"