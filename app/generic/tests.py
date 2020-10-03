from django.test import TestCase
from django.apps import apps
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .apps import GenericConfig
from .models import Data

class GenericConfigTest(TestCase):
    def test_app(self):
        self.assertEqual(GenericConfig.name, "generic")
        self.assertEqual(apps.get_app_config(
            'generic').name, "generic")

class DataTest(TestCase):

    @staticmethod
    def create_data(name="TEST", data="\{'description':'Test data'\}"):
        return Data.objects.create(name=name, data=data)

    def test_create_data(self):
        q = self.create_data()
        self.assertTrue(isinstance(q, Data))
        self.assertEqual(q.__str__(), q.name)

class DataViewSetTest(APITestCase):

    def test_list(self):
        response = self.client.get(reverse('data-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_retrieve(self):
    #     response = self.client.get(reverse('data-detail'), kwargs={'data_pk':'q'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)