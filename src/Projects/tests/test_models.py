from django.test import TestCase

from Projects.models import Project
from Users.models import User


class TestCommentModel(TestCase):
    pass


class TestIssueModel(TestCase):
    pass


class TestProjectModel(TestCase):

    def test_create_project(self):
        self.user = User.objects.create_user(
            username='projectauthor',
            email='test@test.com',
            age=25
        )
        project = Project.objects.create(
            title='Test Project',
            description='A test project description',
            type='BACKEND',
            author=self.user
        )
        self.assertEqual(Project.objects.count(), 1)
        self.assertEqual(project.title, 'Test Project')

    def test_project_have_author(self):
        

    def test_project_str_representation(self):
        pass

    def test_project_contributors_relationship(self):
        pass

    def test_project_only_deleted_by_author(self):
        pass

    def test_project_only_updated_by_author(self):
        pass