from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator


class User(AbstractUser):

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(blank=False, null=False,
                                        # le validator bloque pour l'interface admin
                                      validators=[MinValueValidator(15)]) 
    can_be_contacted = models.BooleanField(default=True)
    can_data_be_shared = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['email', 'age']


class Contributor(models.Model):

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    project = models.ForeignKey('Projects.Project', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
