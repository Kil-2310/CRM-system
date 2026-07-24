from django.test import TestCase
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from crm_system.settings import USER_DATA_TESTING
from .models import Contract

TEST_CONTRACT_DATA = {
    'name': 'Test Contract',
    'start_date': '2026-01-01',
    'end_date': '2027-01-01',
    'cost': 1000,
    'product': 1,
    'file': ''
}


class ContractListTests(TestCase):
    """Тесты получения списка контрактов"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Contract)
        self.permission = Permission.objects.get(
            codename='view_contract',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_contract_list_1(self):
        """Успешный тест получения контрактов"""
        self.user.user_permissions.add(self.permission)

        response = self.client.get(reverse('contract:contract_list'))
        self.assertEqual(response.status_code, 200)

    def test_contract_list_2(self):
        """Провальный тест получения контрактов"""
        response = self.client.get(reverse('contract:contract_list'))
        self.assertEqual(response.status_code, 403)


class ContractDetailTests(TestCase):
    """Тесты получения конкретного контракта"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Contract)
        self.permission = Permission.objects.get(
            codename='view_contract',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_contract_detail_1(self):
        """Успешный тест получения контракта"""
        self.user.user_permissions.add(self.permission)

        response = self.client.get(reverse('contract:contract_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_contract_detail_2(self):
        """Провальный тест получения контракта"""
        response = self.client.get(reverse('contract:contract_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 403)


class ContractCreateTests(TestCase):
    """Тесты создания контракта"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Contract)
        self.permission = Permission.objects.get(
            codename='add_contract',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_contract_create_1(self):
        """Успешное создание контракта"""
        self.user.user_permissions.add(self.permission)

        response = self.client.post(
            reverse('contract:contract_create'),
            data=TEST_CONTRACT_DATA
        )
        self.assertEqual(response.status_code, 302)

    def test_contract_create_2(self):
        """Провальное создание контракта"""
        response = self.client.post(
            reverse('contract:contract_create'),
            data=TEST_CONTRACT_DATA
        )
        self.assertEqual(response.status_code, 403)


class ContractUpdateTests(TestCase):
    """Тесты обновления контракта"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Contract)
        self.permission = Permission.objects.get(
            codename='change_contract',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_contract_update_1(self):
        """Успешное обновление контракта"""
        self.user.user_permissions.add(self.permission)

        new_contract_data = TEST_CONTRACT_DATA.copy()
        new_contract_data['name'] = 'New contract'

        response = self.client.post(
            reverse('contract:contract_update', kwargs={'pk': 1}),
            data=new_contract_data
        )
        self.assertEqual(response.status_code, 302)

    def test_contract_update_2(self):
        """Провальное обновление контракта"""
        new_contract_data = TEST_CONTRACT_DATA.copy()
        new_contract_data['name'] = 'New contract'

        response = self.client.post(
            reverse('contract:contract_update', kwargs={'pk': 1}),
            data=new_contract_data
        )
        self.assertEqual(response.status_code, 403)


class ContractDeleteTests(TestCase):
    """Тесты удаления контракта"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Contract)

        self.permission = Permission.objects.get(
            codename='delete_contract',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_contract_delete_1(self):
        """Успешное удаление контракта"""
        self.user.user_permissions.add(self.permission)

        response = self.client.post(
            reverse('contract:contract_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)

    def test_contract_delete_2(self):
        """Провальное удаление контракта"""
        response = self.client.post(
            reverse('contract:contract_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 403)
