from django.test import TestCase
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from crm_system.settings import USER_DATA_TESTING
from .models import Lead

TEST_LEAD_DATA = {
    'first_name': 'Test',
    'last_name': 'User',
    'email': 'test5@gmail.com',
    'phone': '79991634567',
    'ad': 1
}


class LeadListTests(TestCase):
    """Тесты получения списка потенциальных клиентов"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Lead)
        self.permission = Permission.objects.get(
            codename='view_lead',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_lead_list_1(self):
        """Успешный тест получения потенциальных клиентов"""
        self.user.user_permissions.add(self.permission)

        response = self.client.get(reverse('lead:lead_list'))
        self.assertEqual(response.status_code, 200)

    def test_lead_list_2(self):
        """Провальный тест получения потенциальных клиентов"""
        response = self.client.get(reverse('lead:lead_list'))
        self.assertEqual(response.status_code, 403)


class LeadDetailTests(TestCase):
    """Тесты получения конкретного потенциального клиента"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Lead)
        self.permission = Permission.objects.get(
            codename='view_lead',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_lead_detail_1(self):
        """Успешный тест получения потенциального клиента"""
        self.user.user_permissions.add(self.permission)

        response = self.client.get(reverse('lead:lead_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_lead_detail_2(self):
        """Провальный тест получения потенциального клиента"""
        response = self.client.get(reverse('lead:lead_detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 403)


class LeadCreateTests(TestCase):
    """Тесты создания потенциального клиента"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Lead)
        self.permission = Permission.objects.get(
            codename='add_lead',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_lead_create_1(self):
        """Успешное создание потенциального клиента"""
        self.user.user_permissions.add(self.permission)

        response = self.client.post(
            reverse('lead:lead_create'),
            data=TEST_LEAD_DATA
        )
        self.assertEqual(response.status_code, 302)

    def test_lead_create_2(self):
        """Провальное создание потенциального клиента"""
        response = self.client.post(
            reverse('lead:lead_create'),
            data=TEST_LEAD_DATA
        )
        self.assertEqual(response.status_code, 403)


class LeadUpdateTests(TestCase):
    """Тесты обновления потенциального клиента"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Lead)
        self.permission = Permission.objects.get(
            codename='change_lead',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_lead_update_1(self):
        """Успешное обновление потенциального клиента"""
        self.user.user_permissions.add(self.permission)

        new_lead_data = TEST_LEAD_DATA.copy()
        new_lead_data['first_name'] = 'New name'

        response = self.client.post(
            reverse('lead:lead_update', kwargs={'pk': 1}),
            data=new_lead_data
        )
        self.assertEqual(response.status_code, 302)

    def test_lead_update_2(self):
        """Провальное обновление потенциального клиента"""
        new_lead_data = TEST_LEAD_DATA.copy()
        new_lead_data['first_name'] = 'New name'

        response = self.client.post(
            reverse('lead:lead_update', kwargs={'pk': 1}),
            data=new_lead_data
        )
        self.assertEqual(response.status_code, 403)


class LeadDeleteTests(TestCase):
    """Тесты удаления потенциального клиента"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Lead)

        self.permission = Permission.objects.get(
            codename='delete_lead',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_lead_delete_1(self):
        """Успешное удаление потенциального клиента"""
        self.user.user_permissions.add(self.permission)

        response = self.client.post(
            reverse('lead:lead_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)

    def test_lead_delete_2(self):
        """Провальное удаление потенциального клиента"""
        response = self.client.post(
            reverse('lead:lead_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 403)
