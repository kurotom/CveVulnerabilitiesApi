from django.urls import reverse
from rest_framework.test import APITestCase
from .setUpData import data_testing


class ApiCveidTest(APITestCase):

    @classmethod
    def setUpTestData(self):
        data_testing()

    def test_cveid_bad_cveid_format(self):
        url = f'{reverse("cveid")}?id=CVE-22-010101'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 400)

    def test_cveid_correct_format4(self):
        url = f'{reverse("cveid")}?id=CVE-1111-1111'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_cveid_correct_format5(self):
        url = f'{reverse("cveid")}?id=CVE-1111-11111'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_cveid_correct_format7(self):
        url = f'{reverse("cveid")}?id=CVE-1111-1111111'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
