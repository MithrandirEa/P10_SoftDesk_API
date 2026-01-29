from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError

from Users.models import User, Contributor
from Projects.models import Project

# --- TESTS DES MODELES UTILISATEURS ---


class UserModelTest(TestCase):

    def test_create_user_success(self):
        """Test qu'un user valide est bien créé avec les valeurs par défaut"""
        user = User.objects.create(
            username="testuser",
            email="test@test.com",
            age=25
        )
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.can_be_contacted) # Vérifie le default=True
        self.assertIsNotNone(user.created_time) # Vérifie le auto_now_add

    def test_create_user_duplicate_email_fails(self):
        """Test qu'on ne peut pas créer deux users avec le même email"""
        User.objects.create(username="u1", email="doublon@test.com", age=20)

        # On s'attend à ce que le code suivant lève une erreur d'intégrité
        with self.assertRaises(IntegrityError):
            User.objects.create(username="u2",
                                email="doublon@test.com",
                                age=30)

    def test_no_create_user_underage(self):
        """Test qu'on ne peut pas créer un user avec un age inférieur à 15 ans"""
        user = User.objects.create(username="kiduser",
                                   email="test@test.com",
                                   age=10)

        with self.assertRaises(ValidationError):
            user.full_clean()  # Force la validation des champs
            user.save()


class ContributorModelTest(TestCase):

    def setUp(self):
        # Cette méthode s'exécute avant CHAQUE test. 
        # On prépare un terrain propre avec 1 user et 1 projet.
        self.user = User.objects.create(username='contrib_user',
                                        email='c@test.com',
                                        age=25)
        self.project = Project.objects.create(title='Projet Test',
                                              description='Desc',
                                              type='back-end')

    def test_create_contributor(self):
        """Vérifie qu'on peut lier un user et un projet"""
        contributor = Contributor.objects.create(user=self.user,
                                                 project=self.project)

        # On vérifie la liaison
        self.assertEqual(contributor.user.username, 'contrib_user')
        self.assertEqual(contributor.project.title, 'Projet Test')

    def test_delete_user_cascades(self):
        """Si on supprime l'user, le contributor doit disparaître"""
        Contributor.objects.create(user=self.user, project=self.project)

        # On vérifie qu'il existe
        self.assertEqual(Contributor.objects.count(), 1)

        # On supprime l'user
        self.user.delete()

        # Le contributor doit avoir disparu
        self.assertEqual(Contributor.objects.count(), 0)
