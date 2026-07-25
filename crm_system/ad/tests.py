from django.test import TestCase
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from crm_system.settings import USER_DATA_TESTING
from .models import Ad

TEST_AD_DATA = {
    'name': 'Test Ad Campaign',
    'budget': 10000,
    'channel': 'Facebook',
    'product': 1
}


class AdListTests(TestCase):
    """Тесты получения списка рекламных компаний"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Ad)
        self.permission = Permission.objects.get(
            codename='view_ad',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_ad_list_1(self):
        """Успешный тест получения списка рекламных компаний"""
        self.user.user_permissions.add(self.permission)

        response = self.client.get(reverse('ad:ad_list'))
        self.assertEqual(response.status_code, 200)

    def test_ad_list_2(self):
        """Провальный тест получения списка рекламных компаний"""
        response = self.client.get(reverse('ad:ad_list'))
        self.assertEqual(response.status_code, 403)


class AdDetailTests(TestCase):
    """Тесты получения конкретной рекламной компании"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Ad)
        self.permission = Permission.objects.get(
            codename='view_ad',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_ad_detail_1(self):
        """Успешный тест получения рекламной компании"""
        self.user.user_permissions.add(self.permission)

        response = self.client.get(reverse('ad:ad_detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_ad_detail_2(self):
        """Провальный тест получения рекламной компании"""
        response = self.client.get(reverse('ad:ad_detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 403)


class AdCreateTests(TestCase):
    """Тесты создания рекламной компании"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Ad)
        self.permission = Permission.objects.get(
            codename='add_ad',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_ad_create_1(self):
        """Успешное создание рекламной компании"""
        self.user.user_permissions.add(self.permission)

        response = self.client.post(
            reverse('ad:ad_create'),
            data=TEST_AD_DATA
        )
        self.assertEqual(response.status_code, 302)

    def test_ad_create_2(self):
        """Провальное создание рекламной компании"""
        response = self.client.post(
            reverse('ad:ad_create'),
            data=TEST_AD_DATA
        )
        self.assertEqual(response.status_code, 403)


class AdUpdateTests(TestCase):
    """Тесты обновления рекламной компании"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Ad)
        self.permission = Permission.objects.get(
            codename='change_ad',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_ad_update_1(self):
        """Успешное обновление рекламной компании"""
        self.user.user_permissions.add(self.permission)

        new_ad_data = TEST_AD_DATA.copy()
        new_ad_data['name'] = 'New Ad Campaign Name'

        response = self.client.post(
            reverse('ad:ad_update', kwargs={'pk': 1}),
            data=new_ad_data
        )
        self.assertEqual(response.status_code, 302)

    def test_ad_update_2(self):
        """Провальное обновление рекламной компании"""
        new_ad_data = TEST_AD_DATA.copy()
        new_ad_data['name'] = 'New Ad Campaign Name'

        response = self.client.post(
            reverse('ad:ad_update', kwargs={'pk': 1}),
            data=new_ad_data
        )
        self.assertEqual(response.status_code, 403)


class AdDeleteTests(TestCase):
    """Тесты удаления рекламной компании"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Ad)
        self.permission = Permission.objects.get(
            codename='delete_ad',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_ad_delete_1(self):
        """Успешное удаление рекламной компании"""
        self.user.user_permissions.add(self.permission)

        response = self.client.post(
            reverse('ad:ad_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)

    def test_ad_delete_2(self):
        """Провальное удаление рекламной компании"""
        response = self.client.post(
            reverse('ad:ad_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 403)
