from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """ Test creating a new user with an email is successful """
        email = 'engr.aih@gmail.com'
        password = 'Test123456'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """ Test creating a new user email normalized """
        email = 'aih@gmail.COM'
        # password = 'Test123456'
        user = get_user_model().objects.create_user(
            email,'Test123456'
        )

        self.assertEqual(user.email, email.lower())

    def test_invalid_email(self):
        """ Test  a new user invalid email """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pass123')


    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
        'test@test.com',
        'test123'
    )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff) 
        
               
