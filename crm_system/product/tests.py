from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.urls import reverse

from crm_system.settings import USER_DATA_TESTING


TEDT_PRODUCT_DATA = {
    'id': 1,
    'name': 'Test',
    'description': 'Test',
    'cost': 100
}

TEST_MANAGER_GROUP_DATA = {
    'id': 1,
    'name': 'Managers',
}


class ProductListTest(TestCase):
    """Тест получения спика товаров"""
    fixtures = [
        'site_data.json'
    ]

    def test_product_list_1(self):
        """Успешный тест получения товаров"""
        response = self.client.get(reverse('product:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Мобильное приложение iOS')


class ProductDetailTest(TestCase):
    """Тест получения конкретного товара"""
    fixtures = [
        'site_data.json'
    ]

    def test_product_detail_1(self):
        """Успешный тест получения товаров"""
        response = self.client.get(reverse('product:product_detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Мобильное приложение iOS')


class ProductCreateTests(TestCase):
    """Тесты создания продукта"""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user = User.objects.create_user(
            **USER_DATA_TESTING
        )

        cls.group = Group.objects.create(
            **TEST_MANAGER_GROUP_DATA
        )

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        cls.group.delete()

    def setUp(self):
        self.client.force_login(self.user)

    def test_product_create_1(self):
        """Успешное создание продукта"""
        self.user.groups.add(self.group)

        response = self.client.post(reverse('product:product_create'), data=TEDT_PRODUCT_DATA)
        self.assertEqual(response.status_code, 302)

    def test_product_create_2(self):
        """Провальное создание продукта"""
        response = self.client.post(reverse('product:product_create'), data=TEDT_PRODUCT_DATA)
        self.assertEqual(response.status_code, 403)


class ProductUpdateTests(TestCase):
    """Тесты обновления продукта"""
    fixtures = [
        'site_data.json'
    ]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user = User.objects.create_user(
            **USER_DATA_TESTING
        )

        cls.group = Group.objects.create(
            **TEST_MANAGER_GROUP_DATA
        )

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        cls.group.delete()

    def setUp(self):
        self.client.force_login(self.user)

    def test_product_update_1(self):
        """Успешное обновление продукта"""
        self.user.groups.add(self.group)

        new_product_data = TEDT_PRODUCT_DATA.copy()
        new_product_data['name'] = 'New product'

        response = self.client.post(reverse('product:product_update', kwargs={'pk': 1}), data=new_product_data)
        self.assertEqual(response.status_code, 302)

    def test_product_update_2(self):
        """Провальное обновление продукта"""
        new_product_data = TEDT_PRODUCT_DATA.copy()
        new_product_data['name'] = 'New product'

        response = self.client.post(reverse('product:product_update', kwargs={'pk': 1}), data=new_product_data)
        self.assertEqual(response.status_code, 403)


class ProductDeleteTests(TestCase):
    """Тесты удаления продукта"""
    fixtures = [
        'site_data.json'
    ]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user = User.objects.create_user(
            **USER_DATA_TESTING
        )

        cls.group = Group.objects.create(
            **TEST_MANAGER_GROUP_DATA
        )

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        cls.group.delete()

    def setUp(self):
        self.client.force_login(self.user)

    def test_product_delete_1(self):
        """Успешнле удаление продукта"""
        self.user.groups.add(self.group)

        response = self.client.post(reverse('product:product_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_product_delete_2(self):
        """Провальное удаление продукта"""
        response = self.client.post(reverse('product:product_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 403)
