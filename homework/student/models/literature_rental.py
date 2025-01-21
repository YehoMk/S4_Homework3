from django.db import models

from .access import Access
from .literature import Literature


__all__ = ("LiteratureRental",)


class LiteratureRental(models.Model):
    rent_taker = models.ForeignKey(Access, on_delete=models.CASCADE, related_name="literature_rentals")
    book = models.ForeignKey(Literature, on_delete=models.CASCADE, related_name="literature_rentals")
    rental_date = models.DateTimeField(auto_now=True, null=False)
    rent_giver = models.CharField(null=False, max_length=240)
