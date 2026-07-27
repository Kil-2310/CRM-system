from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from crm_system.settings import USER_DATA_TESTING


class ApplicationMetricsListViewTests(TestCase):
    """Тесты для метрик приложения"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )

    def tearDown(self):
        self.user.delete()

    def test_application_metrics_1(self):
        """Успешный тест получения метрик приложения"""
        self.client.force_login(self.user)

        response = self.client.get(reverse('user:application_metrics_list'))
        self.assertEqual(response.status_code, 200)

    def test_application_metrics_2(self):
        """провальный тест получения метрик приложения"""
        response = self.client.get(reverse('user:application_metrics_list'))
        self.assertEqual(response.status_code, 302)
