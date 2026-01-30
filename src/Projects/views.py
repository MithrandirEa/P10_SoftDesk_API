from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from Projects.models import Comment, Issue, Project
from Projects.serializers import (ProjectDetailSerializer,
                                  ProjectSerializer,
                                  CommentSerializer,
                                  IssueSerializer)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retourne les projets où l'utilisateur connecté est contributeur
        user = self.request.user
        return Project.objects.filter(contributor__user=user)

    def create_project(self, serializer):
        # Associe l'utilisateur connecté comme auteur du projet
        project = serializer.save(author=self.request.user)
        project.contributors.add(self.request.user)


class ProjectDetailViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retourne le détail des projets où l'utilisateur connecté est contributeur
        user = self.request.user
        return Project.objects.filter(contributor__user=user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retourne les commentaires des issues des projets où l'utilisateur connecté est contributeur
        user = self.request.user
        return Comment.objects.filter(project__contributor__user=user)


class IssueViewSet(viewsets.ModelViewSet):

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retourne les issues des projets où l'utilisateur connecté est contributeur
        user = self.request.user
        return Issue.objects.filter(project__contributor__user=user)
