from django.test import TestCase
from django.utils import timezone
from ..models import Menu, Booking
from datetime import datetime
from rest_framework import status

class MenuModelTest(TestCase):
    def setUp(self):
        # Create a sample menu item
        self.menu_item = Menu.objects.create(
            title="Cheeseburger",
            price=8.99,
            inventory=100
        )

    def test_menu_creation(self):
        # Test if the menu item is created properly
        self.assertEqual(self.menu_item.title, "Cheeseburger")
        self.assertEqual(self.menu_item.price, 8.99)
        self.assertEqual(self.menu_item.inventory, 100)

    def test_menu_str(self):
        # Test the string representation of the menu item
        self.assertEqual(str(self.menu_item), "Cheeseburger : 8.99")


class BookingModelTest(TestCase):
    def setUp(self):
        # Create a sample booking item
        self.booking_date = timezone.now().replace(hour=15, minute=0, second=0, microsecond=0)  # 3:00 PM
        self.booking = Booking.objects.create(
            name="John Doe",
            number_of_guests=4,
            booking_date=self.booking_date
        )

    def test_booking_creation(self):
        # Test if the booking is created properly
        self.assertEqual(self.booking.name, "John Doe")
        self.assertEqual(self.booking.number_of_guests, 4)
        self.assertEqual(self.booking.booking_date, self.booking_date)

    def test_booking_str(self):
        # Test the string representation of the booking
        expected_str = f"John Doe for 4 guests on {self.booking_date}"
        self.assertEqual(str(self.booking), expected_str)

    def test_reservation_slot(self):
        # Test the reservation_slot property of the booking
        # It should return the hour of the booking_date
        self.assertEqual(self.booking.reservation_slot, 15)  

