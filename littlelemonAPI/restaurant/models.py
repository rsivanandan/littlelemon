from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu Items'

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'
    
from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Booking Records'

    def __str__(self) -> str:
        return f'{self.name} for {self.number_of_guests} guests on {self.booking_date}'

    @property
    def reservation_slot(self):
        """Returns the hour of the booking_date."""
        return self.booking_date.hour  # Extracts the hour of the booking time
