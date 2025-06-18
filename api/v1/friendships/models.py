from django.db import models
from django.core.exceptions import ValidationError
from api.v1.users.models import User

class Friendship(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships_sent')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships_received')
    creation_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            # Un couple d’utilisateurs ne peut exister qu’une seule fois (pas de doublons).
            models.UniqueConstraint(fields=['user1', 'user2'], name='UC_Friendship_Users'),
            # Les utilisateurs dans une amitié doivent être différents.
            models.CheckConstraint(check=~models.Q(user1=models.F('user2')), name='CHK_Different_Users'),
            # L’ordre des IDs doit toujours être user1_id < user2_id pour éviter les doublons inversés.
            models.CheckConstraint(check=models.Q(user1__lt=models.F('user2')), name='CHK_User_Order'),
        ]
        indexes = [
            models.Index(fields=['user1', 'user2'], name='IDX_Friendships_Users'),
        ]

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        if self.user1 == self.user2:
            raise ValidationError("Users in a friendship must be different.")
        if self.user1.id > self.user2.id:
            raise ValidationError("user1 must have a lower ID than user2 (enforce ordering).")
        

    def __str__(self):
        return f"Friendship between {self.user1} and {self.user2}"