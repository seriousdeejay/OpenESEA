from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=75, unique=True)
    first_name = models.CharField(max_length=50)
    last_name_prefix = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    registered_on = models.DateTimeField(default=now, editable=False)
    # Should add organisations manytomanyfield

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        if not self.last_name_prefix:
            return f"{self.first_name} {self.last_name}"
        return f"{self.first_name} {self.last_name_prefix} {self.last_name}"


class Subscription(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    currency = models.CharField(max_length=255)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name