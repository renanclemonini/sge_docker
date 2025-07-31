from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from . import models
import json


class SupplierViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        self.username = 'teste1'
        self.password = 'senhapadrao'

        # Cria usuário com permissões completas
        self.user = User.objects.create_user(username=self.username, password=self.password)
        permissions = Permission.objects.filter(codename__in=[
            'add_supplier', 'view_supplier', 'change_supplier', 'delete_supplier'
        ])
        self.user.user_permissions.set(permissions)

        # Cria fornecedor para testes
        self.supplier = models.Supplier.objects.create(name="Fornecedor Teste")

        # Obtém token de acesso via JWT
        response = self.client.post(
            '/api/v1/authentication/token/',
            data=json.dumps({'username': self.username, 'password': self.password}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200, msg='Falha ao obter token JWT')

        self.access_token = response.json()['access']
        self.auth_headers = {
            'HTTP_AUTHORIZATION': f'Bearer {self.access_token}',
        }

    # ---------------------- Views HTML (login) ----------------------

    def test_list_view_requires_login(self):
        url = reverse('supplier_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_list_view_with_login_and_permission(self):
        self.client.login(username=self.username, password=self.password)
        url = reverse('supplier_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.supplier.name)

    def test_detail_view(self):
        self.client.login(username=self.username, password=self.password)
        url = reverse('supplier_detail', args=[self.supplier.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.supplier.name)

    def test_create_view(self):
        self.client.login(username=self.username, password=self.password)
        url = reverse('supplier_create')
        response = self.client.post(url, {
            'name': 'Novo Fornecedor',
            'description': 'atualizado'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(models.Supplier.objects.filter(name='Novo Fornecedor').exists())

    def test_update_view(self):
        self.client.login(username=self.username, password=self.password)
        url = reverse('supplier_update', args=[self.supplier.pk])
        response = self.client.post(url, {'name': 'Atualizado'})
        self.assertEqual(response.status_code, 302)
        self.supplier.refresh_from_db()
        self.assertEqual(self.supplier.name, 'Atualizado')

    def test_delete_view(self):
        self.client.login(username=self.username, password=self.password)
        url = reverse('supplier_delete', args=[self.supplier.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(models.Supplier.objects.filter(pk=self.supplier.pk).exists())

    # ---------------------- API Views (JWT) ----------------------

    def test_api_list_suppliers(self):
        url = reverse('suppliers_list_create_api_view')
        response = self.client.get(url, **self.auth_headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.supplier.name, str(response.json()))

    def test_api_create_supplier(self):
        url = reverse('suppliers_list_create_api_view')
        response = self.client.post(
            url,
            data=json.dumps({
                'name': 'Fornecedor via API',
                'description': 'Testando'
            }),
            content_type='application/json',
            **self.auth_headers
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(models.Supplier.objects.filter(name='Fornecedor via API').exists())

    def test_api_retrieve_supplier(self):
        url = reverse('suppliers_retrieve_update_destroy_api_view', args=[self.supplier.pk])
        response = self.client.get(url, **self.auth_headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], self.supplier.name)

    def test_api_update_supplier(self):
        url = reverse('suppliers_retrieve_update_destroy_api_view', args=[self.supplier.pk])
        response = self.client.put(
            url,
            data=json.dumps({'name': 'Atualizado via API'}),
            content_type='application/json',
            **self.auth_headers
        )
        self.assertEqual(response.status_code, 200)
        self.supplier.refresh_from_db()
        self.assertEqual(self.supplier.name, 'Atualizado via API')

    def test_api_delete_supplier(self):
        url = reverse('suppliers_retrieve_update_destroy_api_view', args=[self.supplier.pk])
        response = self.client.delete(url, **self.auth_headers)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(models.Supplier.objects.filter(pk=self.supplier.pk).exists())
