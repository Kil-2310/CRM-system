from django.test import TestCase
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from crm_system.settings import USER_DATA_TESTING
from .models import Customer

TEST_CUSTOMER_DATA = {
    'lead': 2,
}


class CustomerListTests(TestCase):
    """Тесты получения списка активных клиентов"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Customer)
        self.permission = Permission.objects.get(
            codename='view_customer',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_customer_list_1(self):
        """Успешный тест получения активных клиентов"""
        self.user.user_permissions.add(self.permission)

        response = self.client.get(reverse('customer:customer_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Хомяков Евгений')

    def test_customer_list_2(self):
        """Провальный тест получения активных клиентов"""
        response = self.client.get(reverse('customer:customer_list'))
        self.assertEqual(response.status_code, 403)


class CustomerDetailTests(TestCase):
    """Тесты получения конкретного активного клиента"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Customer)
        self.permission = Permission.objects.get(
            codename='view_customer',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_customer_detail_1(self):
        """Успешный тест получения активного клиента"""
        self.user.user_permissions.add(self.permission)

        response = self.client.get(reverse('customer:customer_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Хомяков Евгений')

    def test_customer_detail_2(self):
        """Провальный тест получения активного клиента"""
        response = self.client.get(reverse('customer:customer_detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 403)


class CustomerCreateTests(TestCase):
    """Тесты создания активного клиента"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Customer)
        self.permission = Permission.objects.get(
            codename='add_customer',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_customer_create_1(self):
        """Успешное создание активного клиента"""
        self.user.user_permissions.add(self.permission)

        response = self.client.post(
            reverse('customer:customer_create'),
            data=TEST_CUSTOMER_DATA
        )
        self.assertEqual(response.status_code, 302)

    def test_customer_create_2(self):
        """Провальное создание активного клиента"""
        response = self.client.post(
            reverse('customer:customer_create'),
            data=TEST_CUSTOMER_DATA
        )
        self.assertEqual(response.status_code, 403)


class CustomerUpdateTests(TestCase):
    """Тесты обновления активного клиента"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Customer)
        self.permission = Permission.objects.get(
            codename='change_customer',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_customer_update_1(self):
        """Успешное обновление активного клиента"""
        self.user.user_permissions.add(self.permission)

        new_customer_data = TEST_CUSTOMER_DATA.copy()
        new_customer_data['lead'] = 2

        response = self.client.post(
            reverse('customer:customer_update', kwargs={'pk': 1}),
            data=new_customer_data
        )
        self.assertEqual(response.status_code, 302)

    def test_customer_update_2(self):
        """Провальное обновление активного клиента"""
        new_customer_data = TEST_CUSTOMER_DATA.copy()
        new_customer_data['lead'] = 2

        response = self.client.post(
            reverse('customer:customer_update', kwargs={'pk': 1}),
            data=new_customer_data
        )
        self.assertEqual(response.status_code, 403)


class CustomerDeleteTests(TestCase):
    """Тесты удаления активного клиента"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Customer)
        self.permission = Permission.objects.get(
            codename='delete_customer',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_customer_delete_1(self):
        """Успешное удаление активного клиента"""
        self.user.user_permissions.add(self.permission)

        response = self.client.post(
            reverse('customer:customer_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)

    def test_customer_delete_2(self):
        """Провальное удаление активного клиента"""
        response = self.client.post(
            reverse('customer:customer_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 403)
