from rest_framework import serializers

from Users.models import User, Contributor


# ----------- User Serializers -----------

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'password', 'can_be_contacted',
                  'can_data_be_shared', 'created_time']
        extra_kwargs = {
            'age': {'error_messages': {'min_value': 'L\'âge doit être au'
            ' moins de 15 ans.'}}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# ---------- Contributor Serializer -----------


class ContributorSerializer(serializers.ModelSerializer):

    project_title = serializers.CharField(source='project.title',
                                          read_only=True)
    username = serializers.CharField(source='user.username',
                                     read_only=True)

    class Meta:
        model = Contributor
        fields = ['id', 'user', 'username', 'project', 'project_title']
