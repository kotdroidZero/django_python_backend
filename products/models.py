from locale import currency
from pydoc import describe
from tkinter import CASCADE
from unicodedata import name
from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as PostgresFields

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    icon_url = models.URLField(blank=True)
    description = models.TextField()
    parent_categoty = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        related_name="children_categories",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Currency(models.TextChoices):
        SWEDISH_CROWN = ("SEK", _("Swedish Crown"))
        AMERICAN_DOLLAR = ("USD", _("American Dollar"))
        EURO = ("EUR", _("Euro"))
        POUND_STERLING = ("GBP", _("Pound sterling"))
        YEN = ("JPY", _("Yen"))
        AUD = ("AUD", _("Australian Dollar"))

    title = models.CharField(max_length=512)
    sub_title = models.CharField(max_length=512, blank=True)

    maker = models.ForeignKey(
        Maker, on_delete=models.CASCADE, related_name="products", blank=True, null=True
    )

    image_url1 = models.URLField(blank=True, null=True)
    image_url2 = models.URLField(blank=True, null=True)
    image_url3 = models.URLField(blank=True, null=True)
    image_url4 = models.URLField(blank=True, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.AMERICAN_DOLLAR,
    )

    variation_products_ids = PostgresFields.ArrayField(
        models.IntegerField(null=True, blank=True)
    )

    def __str__(self):
        return f"{self.title} -  {self.sub_title} - {self.maker}"
