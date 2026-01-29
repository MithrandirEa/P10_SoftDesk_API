from django.db import models


class User(models.Model):

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(blank=False, null=False)
    can_be_contacted = models.BooleanField(default=True)
    can_data_be_shared = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)


class Contributor(models.Model):

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    project = models.ForeignKey('Projects.Project', on_delete=models.CASCADE)
