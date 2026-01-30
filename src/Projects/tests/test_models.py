from django.test import TestCase

from Projects.models import Project
from Users.models import User


class TestCommentModel(TestCase):
    pass

class TestIssueModel(TestCase):
    pass

class TestProjectModel(TestCase):

    def test_create_project(self):
        pass

    def test_project_str_representation(self):
        pass

    def test_project_contributors_relationship(self):
        pass

    def test_project_only_deleted_by_author(self):
        pass

    def test_project_only_updated_by_author(self):
        pass