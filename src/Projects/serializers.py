from rest_framework import serializers

from Projects.models import Comment, Issue, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = 'title', 'description', 'type'


class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
