from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    last_activity = models.DateTimeField(default=timezone.now)
    '''
         P.S.
         Probably more flexible approach to implement last_activity field
         would be CustomUser who inherits AbstractBaseUser and has own Manager
         but I chose a way with OneToOne field because of simplicity
         and understanding that this functionality will not grow up
    '''

