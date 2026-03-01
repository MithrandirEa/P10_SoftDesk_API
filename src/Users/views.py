from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView

from Users.models import User, Contributor
from Users.serializers import (UserSerializer,
                               ContributorSerializer)
from Users.permissions import (IsAdminAuthenticated,
                               IsOwner)


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return User.objects.all()

    def get_permissions(self):
        return [IsAuthenticated(), IsOwner()]


class UserSignupView(CreateAPIView):

    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    queryset = User.objects.all()


class ContributorViewSet(ModelViewSet):

    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()


# ----------- ADMIN VIEWS -----------


class AdminUserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAdminAuthenticated]

    def get_queryset(self):
        return User.objects.all()
