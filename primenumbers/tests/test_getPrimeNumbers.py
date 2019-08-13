import json

from django.test import Client, TestCase
from django.urls import reverse


class TestGetPrimeNumbers(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_get_01(self):
        response = self.client.get(reverse("numbers"), data={"n": 10}, )
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.content)
        self.assertEqual(json_data["numbers"], [2, 3, 5, 7])
        self.assertEqual(json_data["count"], 4)
