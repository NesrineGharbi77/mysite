from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    user = models.OneToOneField(User, related_name='Userprofile', on_delete=models.CASCADE)

    def __str__(self):
        return self.User.username