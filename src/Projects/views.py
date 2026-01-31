from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from Projects.models import Comment, Issue, Project
from Projects.serializers import (ProjectDetailSerializer,
                                  ProjectSerializer,
                                  CommentSerializer,
                                  IssueSerializer)
from Users.permissions import IsAdminAuthenticated


#  --------- Project Views ---------

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retourne les projets où l'utilisateur connecté est contributeur
        user = self.request.user
        return Project.objects.filter(contributor__user=user)
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectSerializer

    def create_project(self, serializer):
        # Associe l'utilisateur connecté comme auteur du projet
        project = serializer.save(author=self.request.user)
        project.contributors.add(self.request.user)


class AdminProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsAdminAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectSerializer


#  ----------- Comment Views -----------

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CommentSerializer
        return CommentSerializer

    def get_queryset(self):
        # Retourne les commentaires des issues des projets où l'utilisateur connecté est contributeur
        user = self.request.user
        return Comment.objects.filter(project__contributor__user=user)


# ----------- Issue Views -----------

class IssueViewSet(viewsets.ModelViewSet):

    queryset = Issue.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return IssueSerializer
        return IssueSerializer

    def get_queryset(self):
        # Retourne les issues des projets où l'utilisateur connecté est contributeur
        user = self.request.user
        return Issue.objects.filter(project__contributor__user=user)
