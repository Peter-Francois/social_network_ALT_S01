from django.db import models
from api.v1.users.models import User
from api.v1.user_groups.models import UserGroup

class Message(models.Model):
    content = models.TextField()
    send_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['user'], name='IDX_Messages_User'),
            models.Index(fields=['group'], name='IDX_Messages_Group'),
            models.Index(fields=['send_date'], name='IDX_Messages_Date'),
        ]

    def __str__(self):
        return f"Message by {self.user} in {self.group} at {self.send_date}"