from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from Users.models import User


# ---------- TEST DES PERMISSIONS UTILISATEURS ----------


class UserPermissionsTest(APITestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1",
            email="test@test.com",
            age=25,
            password="password123"
        )
        self.user2 = User.objects.create_user(
            username="intruder",
            email="test2@test.com",
            age=30,
            password="password456"
        )
        self.url = reverse('user-detail', args=[self.user1.id])

    def test_owner_can_access_own_profile(self):

        self.client.force_authenticate(user=self.user1)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_other_user_cannot_access_profile(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_user_cannot_access_profile(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
