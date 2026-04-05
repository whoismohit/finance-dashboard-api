from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('viewer', 'Viewer'),
        ('analyst', 'Analyst'),
        ('admin', 'Admin'),
    )
    #temp = models.CharField(max_length=10, default='x')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')
    #is_active = models.BooleanField(default=True)