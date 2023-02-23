from rest_framework.test import APITestCase
from django.urls import reverse
import json

from .setUpData import data_testing


class ApiQueryTest(APITestCase):

    @classmethod
    def setUpTestData(self):
        data_testing()

    def test_query(self):
        url = f'{reverse("query")}?q=doors'
        response = self.client.get(url, format='json')
        jsonResponse = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(jsonResponse['results'], [])

    def test_query_bad(self):
        url = f'{reverse("query")}?x=algo'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 400)
