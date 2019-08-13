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
        self.assertEqual(json_data["count"], 4)
        self.assertEqual(json_data["numbers"], [2, 3, 5, 7])

    def test_get_02(self):
        response = self.client.get(reverse("numbers"), data={"n": "ten"}, )
        json_data = json.loads(response.content)
        self.assertTrue("errors" in json_data)
        self.assertEqual(json_data["errors"]["n"], ["Enter a whole number."])

    def test_get_03(self):
        response = self.client.get(reverse("numbers"), data={"n": "10", "page": "abc"}, )
        json_data = json.loads(response.content)
        self.assertTrue("errors" in json_data)
        self.assertEqual(json_data["errors"]["page"], ["Enter a whole number."])

    def test_get_04(self):
        response = self.client.get(reverse("numbers"), data={"n": "10", "page_size": "-3"}, )
        json_data = json.loads(response.content)
        self.assertTrue("errors" in json_data)
        self.assertEqual(json_data["errors"]["page_size"], ["Ensure this value is greater than or equal to 1."])

    def test_get_05(self):
        response = self.client.get(reverse("numbers"), data={"n": "10", "start": "-3"}, )
        json_data = json.loads(response.content)
        self.assertTrue("errors" in json_data)
        self.assertEqual(json_data["errors"]["start"], ["Ensure this value is greater than or equal to 1."])

    def test_get_06(self):
        response = self.client.get(reverse("numbers"), data={"n": "10", "page_size": "20", "page": "3"}, )
        json_data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_data["numbers"], [])

