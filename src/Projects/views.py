from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from Projects.models import Comment, Issue, Project
from Projects.serializers import (ProjectDetailSerializer,
                                  ProjectSerializer,
                                  CommentSerializer,
                                  IssueSerializer)
from Users.models import Contributor
from Users.permissions import (IsAdminAuthenticated,
                                IsAuthorOrReadOnly,
                                IsOwner,
                                IsProjectContributor)


#  --------- Project Views ---------

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated,
                          IsProjectContributor,
                          IsAuthorOrReadOnly]

    def get_queryset(self):
        # Retourne les projets où l'utilisateur connecté est contributeur
        user = self.request.user
        return Project.objects.filter(contributor__user=user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectSerializer

    def perform_create(self, serializer):
        # Associe l'utilisateur connecté comme auteur du projet
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(user=self.request.user,
                                   project=project,
                                   role='Author')


class AdminProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsAdminAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        return ProjectSerializer


#  ----------- Comment Views -----------

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,
                          IsProjectContributor,
                          IsAuthorOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        issue_pk = self.kwargs.get('issue_pk')
        project_pk = self.kwargs.get('project_pk')

        return Comment.objects.filter(
            issue__id=issue_pk,
            issue__project__contributor__user=user
        )

    def perform_create(self, serializer):
        issue = Issue.objects.get(pk=self.kwargs.get('issue_pk'))
        serializer.save(author=self.request.user, issue=issue)


# ----------- Issue Views -----------

class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,
                          IsProjectContributor,
                          IsAuthorOrReadOnly]
    serializer_class = IssueSerializer

    def get_queryset(self):
        user = self.request.user
        project_pk = self.kwargs.get('project_pk')

        return Issue.objects.filter(
            project__id=project_pk,
            project__contributor__user=user
        )

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs.get('project_pk'))
        serializer.save(author=self.request.user, project=project)
