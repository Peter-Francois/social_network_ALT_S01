# Generated by Django 5.2.3 on 2025-06-18 14:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared_resources', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_type', models.CharField(choices=[('read', 'Read'), ('write', 'Write'), ('owner', 'Owner')], max_length=20)),
                ('granted_at', models.DateTimeField()),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('granted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='granted_resource_accesses', to=settings.AUTH_USER_MODEL)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accesses', to='shared_resources.sharedresource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource_accesses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ResourceAccess',
                'indexes': [models.Index(fields=['user'], name='idx_user_access')],
                'unique_together': {('resource', 'user')},
            },
        ),
    ]
