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


class TestContributorSerializer(TestCase):
    pass    # TODO: À implémenter
"""Vérifier si : 
    - la création d'un contributeur est toujours associée à un utilisateur existant
    - les champs spécifiques aux contributeurs sont correctement sérialisés et désérialisés
    - la supression d'un contributeur n'affecte pas les données de l'utilisateur associé mais
      bien ses issues et comments
    - un contributor n'a pas accès aux autres projets, issues et comments que ceux auxquels il est assigné"""