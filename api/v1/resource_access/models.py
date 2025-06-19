from django.db import models
from api.v1.users.models import User
from api.v1.shared_resources.models import SharedResource

class ResourceAccess(models.Model):
    ACCESS_TYPE_CHOICES = [
        ('view', 'View'),
        ('edit', 'Edit'),
        ('admin', 'Admin'),
    ]

    access_type = models.CharField(max_length=20, choices=ACCESS_TYPE_CHOICES)
    granted_at = models.DateTimeField()
    expires_at = models.DateTimeField(null=True, blank=True)
    resource = models.ForeignKey(SharedResource, on_delete=models.CASCADE, related_name='accesses')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resource_accesses')
    granted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='granted_resource_accesses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('resource', 'user')
        indexes = [
            models.Index(fields=['user'], name='idx_user_access'),
        ]
        db_table = 'ResourceAccess'

    def __str__(self):
        return f"{self.user} - {self.access_type} access to {self.resource}"