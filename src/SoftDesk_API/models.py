from django.db import models


class User(models.Model):

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(blank=False, null=False)
    role = models.CharField(max_length=50)
    can_be_contacted = models.BooleanField(default=True)
    can_data_be_shared = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)


class Contributor(models.Model):

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)


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
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)