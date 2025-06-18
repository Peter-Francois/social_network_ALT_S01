from django.db import models
from django.conf import settings
from api.v1.publications.models import Publication

class Comment(models.Model):
    content = models.TextField()
    comment_date = models.DateTimeField()

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        # Pour accéder aux commentaires d'un utilisateur
        related_name="comments"
    )

    publication = models.ForeignKey(
        Publication,
        on_delete=models.CASCADE,
        # Pour accéder aux commentaires d'une publication
        related_name="comments"
    )

    # auto_now_add ajoute la date et l'heure lors de la création et n'est pas modifiable
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now ajoute la date et l'heure lors de la modification et est modifiable
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['user'], name='idx_comments_user'),
            models.Index(fields=['publication'], name='idx_comments_publication'),
            models.Index(fields=['comment_date'], name='idx_comments_date'),
        ]
        ordering = ['-comment_date']

    def __str__(self):
        return f"Comment by {self.user} on {self.publication}"