from django.db import models
from django.utils import timezone
from api.v1.users.models import User
from api.v1.user_groups.models import UserGroup

class GroupMember(models.Model):
    join_date = models.DateTimeField()
    member_status = models.CharField(max_length=20)
    member_role = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_memberships')
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, related_name='members')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'group')
        indexes = [
            models.Index(fields=['user'], name='IDX_GroupMembers_User'),
            models.Index(fields=['group'], name='IDX_GroupMembers_Group'),
            models.Index(fields=['member_status'], name='IDX_GroupMembers_Status'),
        ]

    def __str__(self):
        return f"{self.user} in {self.group} as {self.member_role} ({self.member_status})"