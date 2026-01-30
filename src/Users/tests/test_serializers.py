from django.test import TestCase

from Users.models import User
from Users.serializers import (UserDetailSerializer,
                               UserSerializer)

# ------- TESTS DES SERIALIZERS ------- 


class TestUserSerializer(TestCase):

    def test_age_rejection_serializer(self):
        invalid_data = {
            'username': 'testuser',
            'email': 'test@test.com',
            'age': 10
        }

        serializer = UserSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('age', serializer.errors)

    def test_no_clear_password_serializer(self):
        user = User.objects.create_user(
            username='testuser2',
            email='test@test.com',
            age=30,
            password='securepassword123'
        )
        serializer = UserSerializer(user)
        # Verifie que le psw n'est pas dans les données en claires
        self.assertNotIn('password', serializer.data)


class TestUserDetailSerializer(TestCase):

    def test_detailed_fields_serializer(self):
        user_data = {
            'username': 'detaileduser',
            'email': 'test@test.com',
            'age': 25,
            'can_be_contacted': True,
            'can_data_be_shared': False,
            'created_time': '2024-01-01T12:00:00Z'
        }
        serializer = UserDetailSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(set(serializer.validated_data.keys()),
                         {'username', 'email', 'age', 'can_be_contacted',
                          'can_data_be_shared', 'created_time'})

    def test_no_clear_password_detailed_serializer(self):
        user = User.objects.create_user(
            username='testuser2',
            email='test@test.com',
            age=30,
            password='securepassword123'
        )
        serializer = UserDetailSerializer(user)
        # Verifie que le psw n'est pas dans les données detaillees en claires
        self.assertNotIn('password', serializer.data)


class TestContributorSerializer(TestCase):
    pass    # TODO: À implémenter
