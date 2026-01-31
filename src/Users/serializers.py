from rest_framework import serializers

from Users.models import User, Contributor


# ----------- User Serializers -----------

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age']
        extra_kwargs = {
            'age': {'error_messages': {'min_value': 'L\'âge doit être au'
            ' moins de 15 ans.'}}
        }


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'can_be_contacted',
                  'can_data_be_shared', 'created_time']


# ---------- Contributor Serializer -----------


class ContributorSerializer(serializers.ModelSerializer):

    project_title = serializers.CharField(source='project.title',
                                          read_only=True)
    username = serializers.CharField(source='user.username',
                                     read_only=True)

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'username', 'project', 'project_title']
