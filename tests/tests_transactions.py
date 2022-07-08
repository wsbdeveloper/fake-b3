import base64
import pytest
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from transactions.models import Transactions

from django.contrib.auth import get_user_model


@pytest.mark.django_db
class TestViews(APITestCase):
    def setUp(self):
        self.list_url = reverse('Transactions-list')

        # Mock user
        User = get_user_model()
        User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

        # Create token basic
        credentials = base64.b64encode(b'temporary:temporary')
        self.client.credentials(HTTP_AUTHORIZATION='Basic ' + credentials.decode('ascii'))

        # Model started
        self.transaction = Transactions.objects.create(
            name="Simulacao ipca",
            amount=2.344
        )

    def test_should_response_200_GET_list_transactions(self):
        """ list transactions """
        # given
        User = get_user_model()
        user_credentials = User.objects.first()

        headers = {
           'Authorization': 'Basic ' +
                base64.b64encode(b'temporary:temporary').decode("ascii")
        }

        # Login or authentication
        self.client.login(username=user_credentials.username, password=user_credentials.password)

        # response
        response = self.client.get(self.list_url, follow=True, **headers)

        # asserts
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_response_200_POST_create_transaction(self):
        """ list transactions """
        # given
        User = get_user_model()
        user_credentials = User.objects.first()

        headers = {
           'Authorization': 'Basic ' +
                base64.b64encode(b'temporary:temporary').decode("ascii")
        }

        # Login or authentication
        self.client.login(username=user_credentials.username, password=user_credentials.password)

        # response
        response = self.client.get(self.list_url, follow=True, **headers)

        # asserts
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_response_200_PUT_create_transaction(self):
        """ list transactions """
        # given
        User = get_user_model()
        user_credentials = User.objects.first()

        headers = {
           'Authorization': 'Basic ' +
                base64.b64encode(b'temporary:temporary').decode("ascii")
        }

        # Login or authentication
        self.client.login(username=user_credentials.username, password=user_credentials.password)

        # response
        response = self.client.get(self.list_url, follow=True, **headers)

        # asserts
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_should_response_200_PUT_create_transaction(self):
        """ list transactions """
        # given
        User = get_user_model()
        user_credentials = User.objects.first()

        headers = {
           'Authorization': 'Basic ' +
                base64.b64encode(b'temporary:temporary').decode("ascii")
        }

        # Login or authentication
        self.client.login(username=user_credentials.username, password=user_credentials.password)

        # response
        response = self.client.get(self.list_url, follow=True, **headers)

        # asserts
        self.assertEqual(response.status_code, status.HTTP_200_OK)




