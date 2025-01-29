from django.test import TestCase
from django.urls import reverse

class UserTests(TestCase):
    def test_register_user(self):
        response = self.client.post(reverse('register'), {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password': 'securepassword123',
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Usuario registrado con éxito', response.json()['message'])
