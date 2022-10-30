from django.core.validators import MinValueValidator
from django.db import models
from menu.models import Sections


class Items(models.Model):
    item_name = models.CharField(max_length=150, unique=True, blank=False)
    description = models.TextField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[
                                MinValueValidator(1.00)])
    from_section = models.ForeignKey(
        Sections, related_name='items', on_delete=models.CASCADE, null=False, blank=False)
    modifiers = models.ManyToManyField("menu.Modifiers", blank=True)

    def __str__(self):
        return str(self.id)
