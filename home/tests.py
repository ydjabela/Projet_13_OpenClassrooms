import pytest
from django.test import TestCase
from django.urls import reverse


class TestsHomepage(TestCase):

    def test_home_index(self):
        response = self.client.get(reverse('homes:homes_index'))
        attempted_contain = b'<title>Holiday Homes</title>'
        self.assertEqual(True, attempted_contain in response.content)
