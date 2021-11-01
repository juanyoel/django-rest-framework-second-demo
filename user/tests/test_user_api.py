from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
ME_URL = reverse('user:me')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Testear el API Publica del usuario"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Probar crear usuario con un payload exitoso"""
        payload = {
            'email': 'test@test.com',
            'password': 'testtopass',
            'name': 'Test name'
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Probar crear un usuario que ya existe falla"""
        payload = {
            'email': 'test@test.com',
            'password': 'Testpass123',
            'name': 'Test name'
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """La contraseña debe ser mayor a 5 caracteres"""
        payload = {
            'email': 'test@test.com',
            'password': 'pw',
            'name': 'Test name'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Probar que el token sea creado para el usuario"""
        payload = {
            'email': 'test@test.com',
            'password': 'pw',
            'name': 'Test name'
        }
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Probar que el token no es creado con credenciales invalidas"""
        create_user(email='test@test.com', password='Testpass123')
        payload = {'email': 'test@test.com', 'password': 'wrong'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_no_user(self):
        """Prueba que no se crea un token si no existe el usuario"""
        payload = {
            'email': 'test@test.com',
            'password': 'pw',
            'name': 'Test name'
        }
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Prueba que no se crea el usuario"""
        payload = {'email': 'test@test.com', 'password': 'testpass'}
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_field(self):
        """Probar que el email y contrasena sean requeridos"""
        res = self.client.post(TOKEN_URL, {'email': 'one', 'password': ''})

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized(self):
        """Prueba que la autenticación sea requerida para los usuarios"""
        res = self.client.get(ME_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


    class PrivateUserApiTest(TestCase):
        """Testear el api privada del usuario"""

        def setUp(self):
            self.user = create_user(
                email='test@test.com',
                password='password',
                name='name'
            )
            self.client = APIClient()
            self.client.force_authenticate(user=self.user)

        def test_retrieve_profile_success(self):
            """Probar obtener perfil para usuario con login"""
            res = self.client.get(ME_URL)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(res.data, {
                'name': self.user.name,
                'email': self.user.email
            })

        def test_post_me_not_allowed(self):
            """Pruba que el post no sea permitido"""
            res = self.client.post(ME_URL, {})
            self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        def test_update_user_profile(self):
            """Probar que el usuario esta siendo actualizado si esta siendo actualizado"""
            payload = {'name': 'new name', 'password': "newpass1234"}

            res = self.client.patch(ME_URL, payload)

            self.user.refresh_from_db()
            self.assertEqual(self.user.name, payload['name'])
            self.assertTrue(self.user.check_password(payload['password']))
            self.assertEqual(res.status_code, status.HTTP_200_OK)

