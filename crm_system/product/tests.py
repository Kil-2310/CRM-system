from django.test import TestCase
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from crm_system.settings import USER_DATA_TESTING
from .models import Product

TEST_PRODUCT_DATA = {
    'name': 'Test',
    'description': 'Test',
    'cost': 100
}


class ProductListTests(TestCase):
    """Тесты получения списка товаров"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Product)
        self.permission = Permission.objects.get(
            codename='view_product',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_product_list_1(self):
        """Успешный тест получения товаров"""
        self.user.user_permissions.add(self.permission)

        response = self.client.get(reverse('product:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Мобильное приложение iOS')

    def test_product_list_2(self):
        """Провальный тест получения товаров"""
        response = self.client.get(reverse('product:product_list'))
        self.assertEqual(response.status_code, 403)


class ProductDetailTests(TestCase):
    """Тесты получения конкретного товара"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Product)
        self.permission = Permission.objects.get(
            codename='view_product',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_product_detail_1(self):
        """Успешный тест получения товара"""
        self.user.user_permissions.add(self.permission)

        response = self.client.get(reverse('product:product_detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Мобильное приложение iOS')

    def test_product_detail_2(self):
        """Провальный тест получения товара"""
        response = self.client.get(reverse('product:product_detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 403)


class ProductCreateTests(TestCase):
    """Тесты создания продукта"""

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Product)
        self.permission = Permission.objects.get(
            codename='add_product',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_product_create_1(self):
        """Успешное создание продукта"""
        self.user.user_permissions.add(self.permission)

        response = self.client.post(
            reverse('product:product_create'),
            data=TEST_PRODUCT_DATA
        )
        self.assertEqual(response.status_code, 302)  # Redirect после создания

    def test_product_create_2(self):
        """Провальное создание продукта"""
        response = self.client.post(
            reverse('product:product_create'),
            data=TEST_PRODUCT_DATA
        )
        self.assertEqual(response.status_code, 403)


class ProductUpdateTests(TestCase):
    """Тесты обновления продукта"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Product)
        self.permission = Permission.objects.get(
            codename='change_product',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_product_update_1(self):
        """Успешное обновление продукта"""
        self.user.user_permissions.add(self.permission)

        new_product_data = TEST_PRODUCT_DATA.copy()
        new_product_data['name'] = 'New product'

        response = self.client.post(
            reverse('product:product_update', kwargs={'pk': 1}),
            data=new_product_data
        )
        self.assertEqual(response.status_code, 302)

    def test_product_update_2(self):
        """Провальное обновление продукта"""
        new_product_data = TEST_PRODUCT_DATA.copy()
        new_product_data['name'] = 'New product'

        response = self.client.post(
            reverse('product:product_update', kwargs={'pk': 1}),
            data=new_product_data
        )
        self.assertEqual(response.status_code, 403)


class ProductDeleteTests(TestCase):
    """Тесты удаления продукта"""
    fixtures = ['site_data.json']

    def setUp(self):
        self.user = User.objects.create_user(
            **USER_DATA_TESTING
        )
        self.client.force_login(self.user)

        content_type = ContentType.objects.get_for_model(Product)

        self.permission = Permission.objects.get(
            codename='delete_product',
            content_type=content_type,
        )

    def tearDown(self):
        self.user.delete()

    def test_product_delete_1(self):
        """Успешное удаление продукта"""
        self.user.user_permissions.add(self.permission)

        response = self.client.post(
            reverse('product:product_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)

    def test_product_delete_2(self):
        """Провальное удаление продукта"""
        response = self.client.post(
            reverse('product:product_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 403)
