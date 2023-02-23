from django.test import TestCase
from api.models import CveModel

from .setUpData import data_testing


class CveModelTest(TestCase):

    @classmethod
    def setUpTestData(self):
        data_testing()

    def test_fields_data_object(self):
        obj = CveModel.objects.get(id=1)
        self.assertEqual(obj.name, "CVE-0000")
        self.assertEqual(obj.phase, " ")
