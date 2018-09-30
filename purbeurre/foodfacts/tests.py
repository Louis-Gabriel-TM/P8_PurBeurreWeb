from django.test import TestCase
from django.urls import reverse


class TestViewsStatusCode(TestCase):
    """Test that index, disclaimer, my_products and results pages
    return a HTTP 200 status code
    """

    def test_index_page_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_disclaimer_page_status_code(self):
        response = self.client.get(reverse('disclaimer'))
        self.assertEqual(response.status_code, 200)

    def test_my_products_page_status_code(self):
        response = self.client.get(reverse('my_products'))
        self.assertEqual(response.status_code, 200)

    def test_results_page_status_code(self):
        response = self.client.get(reverse('results'))
        self.assertEqual(response.status_code, 200)

    # test that details page return 200 if the product exists

    # test that details page return 404 if the product does not exist


class TestUserCreation(TestCase):
    pass


class TestSavingASubstitute(TestCase):
    pass
