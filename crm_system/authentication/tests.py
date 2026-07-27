from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from crm_system.settings import USER_DATA_TESTING


class LoginTests(TestCase):
    """Тесты аутентификации пользователя"""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user = User.objects.create_user(
            **USER_DATA_TESTING
        )

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def test_login_1(self):
        """Успешный тест аутентификации"""
        response = self.client.post(reverse('authentication:login'), data=USER_DATA_TESTING)
        self.assertEqual(response.status_code, 302)

    # def test_login_2(self):
    #     """Провальный тест аутентификации"""
    #     fake_user_data = USER_DATA_TESTING
    #     fake_user_data['password'] = '333'
    #
    #     response = self.client.post(reverse('authentication:login'), data=fake_user_data)
    #     self.assertEqual(response.status_code, 302)


class LogoutTest(TestCase):
    """Тест выхода из аккаунта клиента"""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user = User.objects.create_user(
            **USER_DATA_TESTING
        )

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        self.client.force_login(self.user)

    def test_logout_1(self):
        """Успешный тест выхода из аккаунта"""
        response = self.client.post(reverse('authentication:logout'))
        self.assertEqual(response.status_code, 302)
