from rest_framework.test import APITestCase
from api.models import CveModel
from django.urls import reverse
import json

from .setUpData import data_testing


class ApiDateTest(APITestCase):

    @classmethod
    def setUpTestData(self):
        data_testing()

    def test_date_only_start(self):
        url = f'{reverse("date")}?start=2000-01-01'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_date_only_end(self):
        url = f'{reverse("date")}?end=2000-01-01'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 400)

    def test_date_start_gt_end(self):
        url = f'{reverse("date")}?start=2000-01-01&end=2023-01-01'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_date_start_lt_end(self):
        url = f'{reverse("date")}?start=2023-01-01&end=2000-01-01'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 400)
