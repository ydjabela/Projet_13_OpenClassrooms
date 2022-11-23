from django.test import TestCase
from .models import Address, Letting
from django.urls import reverse


class TestsLettings(TestCase):
    def setUp(self) -> None:
        """Initialize models
        """
        # Address test
        address = Address(**{
            'id': 1,
            'number': 1,
            'street': 'street_1',
            'city': 'city_1',
            'state': 'state_1',
            'zip_code': 11111,
            'country_iso_code': 'France',
        })
        address.save()

        # Letting test
        letting = Letting(**{
            'id': 1,
            'title': 'test_letting',
            'address_id': 1
        })
        letting.save()

    def test_lettings_index(self):
        response = self.client.get(reverse('lettings:lettings_index'))
        attempted_contain = b'<title>Lettings</title>'
        self.assertEqual(True, attempted_contain in response.content)

    def test_lettings_letting(self):
        letting_id = '1'
        response = self.client.get(
            reverse('lettings:letting',
                    kwargs={'letting_id': letting_id})
                )
        title = 'test_letting'
        attempted_contain = bytes(
            f"<title>{title}</title>", 'utf-8')
        self.assertEqual(True, attempted_contain in response.content)


class AdressTestCase(TestCase):
    def setUp(self):
        Address.objects.create(
            number=2,
            street="Flandre",
            city="Paris",
            state="France",
            zip_code=75019,
            country_iso_code=12
        )

    def test_adress(self):
        Address.objects.get(street="Flandre")
