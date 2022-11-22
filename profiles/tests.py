# Django Libs:
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
# Local Libs:
from .models import Profile


class TestsProfiles(TestCase):
    def setUp(self) -> None:
        # User test
        user = User.objects.create_user(**{
            'id': 1,
            'username': 'test_user',
            'email': 'test_email@test.com',
            'password': 'Motdepasse123'
        })
        user.save()
        # Profile test
        profile = Profile(
            **{'id': 1,
               'favorite_city': 'Test City',
               'user_id': 1,
               })
        profile.save()

    def test_profiles_index(self):
        response = self.client.get(reverse('profiles:profiles_index'))
        attempted_contain = b'<title>Profiles</title>'
        self.assertEqual(True, attempted_contain in response.content)

    def test_profiles_profile(self):
        username = 'test_user'
        response = self.client.get(reverse(
            'profiles:profile',
            kwargs={'username': username})
        )
        attempted_contain = bytes(
            f"<title>{username}</title>", 'utf-8')
        self.assertEqual(True, attempted_contain in response.content)
