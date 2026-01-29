from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from Users.models import User, Contributor
from Users.serializers import (UserSerializer,
                               UserDetailSerializer,
                               ContributorSerializer)
from Users.permissions import IsOwner


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    detail_serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_permissions(self):
        return [IsAuthenticated(), IsOwner()]


class ContributorViewSet(ModelViewSet):
    """ ATTENTION: bien réfléchir à comment lier contributeur, user(author), 
    users (ceux aui consultent) et projet """
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()
