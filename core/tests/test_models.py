from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='testuser@sid.com', password='testpass123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating user with an email is successfull"""
        email = 'testemail@sid.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""

        email = 'testemail@SID.COM'
        user = get_user_model().objects.create_user(email, 'testpass12345')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """Test creating a user with no email raise error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password='testpass123')

    def test_user_password(self):
        """Test creating a user with no password raise error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email='testemail@sid.com', password=None)

    def test_create_new_superuser(self):
        """Test creating new superuser"""

        user = get_user_model().objects.create_superuser(
            email='testsuperuser.sid.com',
            password='testpasssupper123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Indian'
        )

        self.assertEqual(str(tag), tag.name)