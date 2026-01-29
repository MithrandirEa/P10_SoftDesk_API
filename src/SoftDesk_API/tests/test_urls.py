from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.views.generic import RedirectView

# --- TESTS DES URLS ---


class TestUrls(SimpleTestCase):

    def test_token_obtain_pair(self):
        url = reverse('token_obtain_pair')
        self.assertEqual(url, '/api/token/')
        self.assertEqual(resolve(url).func.view_class, TokenObtainPairView)

    def test_token_refresh(self):
        url = reverse('token_refresh')
        self.assertEqual(url, '/api/token/refresh/')
        self.assertEqual(resolve(url).func.view_class, TokenRefreshView)

    def test_admin_url(self):
        url = reverse('admin:index')
        self.assertEqual(url, '/admin/')
        self.assertEqual(resolve(url).func.__name__, 'index')

    def test_root(self):
        url = reverse('root')
        self.assertEqual(url, '/')
        self.assertEqual(resolve(url).func.view_class, RedirectView)
