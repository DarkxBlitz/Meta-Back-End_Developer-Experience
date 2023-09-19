from django.test import TestCase
from .models import Menu

class MenuModelTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="Seafood Marinara Pasta", price=13)
        self.assertEqual(item, "Seafood Marinara Pasta : 13")
