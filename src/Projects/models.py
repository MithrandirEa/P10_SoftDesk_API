from django.db import models

from Users.models import Contributor, User


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=50)
    contributors = models.ManyToManyField(User, through=Contributor)
    created_time = models.DateTimeField(auto_now_add=True)


class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    priority = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE)
    author = models.ForeignKey('Users.User', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)