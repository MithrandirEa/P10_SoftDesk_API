from django.db import models

from Users.models import Contributor, User


class Comment(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False)
    description = models.TextField()
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE)
    author = models.ForeignKey('Users.User',
                               on_delete=models.CASCADE,
                               related_name='created_comments')
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Issue(models.Model):

    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    TAG_CHOICES = [
        ('BUG', 'Bug'),
        ('FEATURE', 'Feature'),
        ('TASK', 'Task'),
    ]

    STATUS_CHOICES = [
        ('TO_DO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('FINISHED', 'Finished'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    author = models.ForeignKey('Users.User',
                               on_delete=models.CASCADE,
                               related_name='created_issues')
    created_time = models.DateTimeField(auto_now_add=True)


class Project(models.Model):

    PROJECT_TYPES = [
        ('BACKEND', 'Backend'),
        ('FRONTEND', 'Frontend'),
        ('IOS', 'iOS'),
        ('ANDROID', 'Android'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    type = models.CharField(max_length=50, choices=PROJECT_TYPES)
    contributors = models.ManyToManyField(User,
                                          through=Contributor,
                                          related_name='contributed_projects')
    author = models.ForeignKey('Users.User',
                               on_delete=models.CASCADE,
                               related_name='created_projects')
    created_time = models.DateTimeField(auto_now_add=True)
