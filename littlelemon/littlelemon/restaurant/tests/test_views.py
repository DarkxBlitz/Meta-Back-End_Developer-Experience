from django.test import TestCase
from .views import Menu, Booking
from datetime import datetime

class BookingTest(TestCase):

    def test_create_booking(self):
        booking = Booking.objects.create(
            name="Billy Bob",
            booking_date=datetime(2023, 9, 20)
        )
        expected_str = "Billy Bob - 1 PM"
        self.assertEqual(str(booking), expected_str)