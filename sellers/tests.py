import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Seller

def create_seller(seller, days):
    time = timezone.now() + datetime.timedelta(days = days)
    create_first_name, create_last_name = seller.split()
    
    return Seller.objects.create(first_name = create_first_name, last_name = create_last_name, regist_date = time)

class SellerModelTests(TestCase):
    def test_was_published_recently_with_future_seller(self):
        time = timezone.now() + datetime.timedelta(days = 30)
        future_seller = Seller(regist_date = time)
        self.assertIs(future_seller.was_published_recently(), False)
        
    def test_was_published_recently_with_old_seller(self):
        time = timezone.now() - datetime.timedelta(days = 1, seconds = 1)
        old_seller = Seller(regist_date = time)
        self.assertIs(old_seller.was_published_recently(), False)
    
    def test_was_published_recently_with_recent_seller(self):
        time = timezone.now() - datetime.timedelta(hours = 23, minutes = 59, seconds = 59)
        recent_seller = Seller(regist_date = time)
        self.assertIs(recent_seller.was_published_recently(), True)
    
class SellerIndexViewTests(TestCase):
    def test_no_seller(self):
        response = self.client.get(reverse('sellers:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No products are available.")
        self.assertQuerysetEqual(response.context['latest_seller_list'], [])
    
    def test_past_seller(self):
        seller = create_seller(seller="Past Name", days = -30)
        response = self.client.get(reverse('sellers:index'))
        self.assertQuerysetEqual(
            response.context['latest_seller_list'],
            [seller],
        )
    
    def test_future_seller(self):
        create_seller(seller="Future Name", days = 30)
        response = self.client.get(reverse('sellers:index'))
        self.assertContains(response, "No products are available.")
        self.assertQuerysetEqual(response.context['latest_seller_list'], [])
    
    def test_future_seller_and_past_seller(self):
        seller = create_seller(seller="Past Name", days = -30)
        create_seller(seller="Future Name", days = 30)
        response = self.client.get(reverse('sellers:index'))
        self.assertQuerysetEqual(
            response.context['latest_seller_list'],
            [seller],
        )
    
    def test_two_past_seller(self):
        seller1 = create_seller(seller="Past Name", days = -30)
        seller2 = create_seller(seller="Past NamePrime", days = -5)
        response = self.client.get(reverse('sellers:index'))
        self.assertQuerysetEqual(
            response.context['latest_seller_list'],
            [seller2, seller1],
        )

class SellerDetailViewTests(TestCase):
    def test_future_seller(self):
        future_seller = create_seller(seller = "Future Name", days = 5)
        url = reverse("sellers:detail", args = (future_seller.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_past_question(self):
        past_seller = create_seller(seller = "Past Name", days = -5)
        url = reverse("sellers:detail", args = (past_seller.id,))
        response = self.client.get(url)
        self.assertContains(response, past_seller)
        
class SellerResultsViewTests(TestCase):
    def test_future_seller(self):
        future_seller = create_seller(seller = "Future Name", days = 5)
        url = reverse("sellers:results", args = (future_seller.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_past_question(self):
        past_seller = create_seller(seller = "Past Name", days = -5)
        url = reverse("sellers:results", args = (past_seller.id,))
        response = self.client.get(url)
        self.assertContains(response, past_seller)