from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from django.test import TestCase, Client


from Users.models import User


class LoginMixin:
    def login_and_get_headers(self):
        login_data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post('/api/token/',
                                    login_data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        access_token = response.json().get('access')
        return {
            'HTTP_AUTHORIZATION': f'Bearer {access_token}',
        }


# ---------- TESTS DES VIEWS ----------
class TestUserViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.username = 'testuser888'
        self.password = 'testpassword888'
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email='testuser888@example.com',
            age=25
        )

    def test_signup_user(self):
        user_data = {
            'username': 'testCreateUser',
            'email': 'testuser@example.com',
            'age': 30,
            'password': 'testpassword'
        }
        response = self.client.post('/signup/',
                                    user_data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)

        user_exists = User.objects.filter(username='testCreateUser').exists()
        self.assertTrue(user_exists)

    def test_login_user(self):
        user_data = {
            'username': self.username,
            'password': self.password
        }
        response = self.client.post('/api/token/',
                                    user_data,
                                    content_type='application/json')
        self.assertEqual(response.status_code, HTTP_200_OK)

        response_data = response.json()
        self.assertIn('access', response_data)
        self.assertIn('refresh', response_data)

    def test_users_list_no_authentication(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 401)

    def test_user_detail_no_authentication(self):
        response = self.client.get(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, 401)

    def test_users_list_with_authentication(self):
        auth_headers = self.login_and_get_headers()
        response = self.client.get('/api/users/', **auth_headers)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_user_detail_with_authentication(self):
        auth_headers = self.login_and_get_headers()
        response = self.client.get(f'/api/users/{self.user.id}/',
                                   **auth_headers)
        self.assertEqual(response.status_code, HTTP_200_OK)
