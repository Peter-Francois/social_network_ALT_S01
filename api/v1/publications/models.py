from django.db import models
from django.conf import settings

class Publication(models.Model):
    content = models.TextField()
    publication_date = models.DateTimeField()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # Pour supprimer les publications d'un utilisateur lorsqu'il est supprimé
        on_delete=models.CASCADE,
        # Pour accéder aux publications d'un utilisateur
        related_name="publications"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["publication_date"]),
        ]
        ordering = ["-publication_date"]

    def __str__(self):
        return f"Publication #{self.id} by {self.user}"