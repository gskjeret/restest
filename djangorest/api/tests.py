from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Customer


class ModelTestCase(TestCase):
    """This class defines the test suite for the customer model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.customer_name = "R. Fant AS"
        self.postnr = 1000
        self.customer = Customer(name=self.customer_name, postnr=self.postnr)

    def test_model_can_create_a_customer(self):
        """Test the customer model can create a customer."""
        old_count = Customer.objects.count()
        self.customer.save()
        new_count = Customer.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.customer_data = {'name': 'S.Vindel & Co', 'postnr': 1001}
        self.response = self.client.post(
            reverse('create'),
            self.customer_data,
            format="json")

    def test_api_can_create_a_customer(self):
        """Test the api has customer creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
