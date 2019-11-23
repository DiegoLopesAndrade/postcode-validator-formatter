from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import index, check


class IndexTests(SimpleTestCase):
    """Test to validade index function view"""

    def setUp(self):
        url = reverse('index')
        self.response = self.client.get(url)

    def test_index_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_template(self):
        self.assertTemplateUsed(self. response, 'validate_postcode.html')

    def test_index_contains_correct_html(self):
        self.assertContains(self.response, 'UK Postcode Validator')

    def test_index_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! T should not be on the page.')


class CheckTests(SimpleTestCase):
    """Test to validade check function view"""

    def setUp(self):
        url = reverse('check')
        self.response = self.client.get(url)

    def test_check_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_check_template(self):
        self.assertTemplateUsed(self.response, 'validate_postcode.html')
