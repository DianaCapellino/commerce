from django.contrib.auth.models import AbstractUser
from django.db import models
import django.utils.timezone


class User(AbstractUser):
    birthday = models.DateTimeField(default=django.utils.timezone.now, verbose_name='date of birth')
    
    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"

#class Listing(models.Model):
#    id = models.
    