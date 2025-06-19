from django.db import models
from api.v1.users.models import User

class SharedResource(models.Model):
    RESOURCE_TYPE_CHOICES = [
        ('document', 'Document'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('presentation', 'Presentation'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)
    path = models.TextField()
    mime_type = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    is_public = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_resources')
    # Clé étrangère vers le même modèle (pour les dossiers et fichiers)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    metadata = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['resource_type'], name='idx_resource_type'),
            models.Index(fields=['creator'], name='idx_creator_resources'),
        ]
        db_table = 'SharedResources'

    def __str__(self):
        return self.title