from django.core.exceptions import ValidationError
from django.core.validators import (
    EmailValidator,
    MinLengthValidator
)
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from app_superstore.validators import only_letters_validator, phone_number_validator

FIRST_NAME_MAX_LENGTH = 30
LAST_NAME_MAX_LENGTH = 40
USER_MAX_LENGTH = 20
EMAIL_MAX_LENGTH = 30
PHONE_NUMBER_MAX_LENGTH = 10
CITY_MAX_LENGTH = 20
ADDRESS_MAX_LENGTH = 50

NAMES_MIN_LENGTH = 2
ADDRESS_MIN_LENGTH = 5

class UserProfile(models.Model):

    COUNTRIES = (
        "Bulgaria",
        "China",
        "Netherlands"
    )
    COUNTRIES_CHOICES = [(x, x) for x in COUNTRIES]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        default='',
        validators=(
            MinLengthValidator(NAMES_MIN_LENGTH),
            only_letters_validator,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        default='',
        validators=(
            MinLengthValidator(NAMES_MIN_LENGTH),
            only_letters_validator,
        ),
    )

    username = models.CharField(
        max_length=USER_MAX_LENGTH,
        default='',
        validators=(
            MinLengthValidator(NAMES_MIN_LENGTH),
        ),
    )

    email = models.CharField(
        max_length=EMAIL_MAX_LENGTH,
        default='',
        validators=(
            EmailValidator,
        ),
    )

    phone_number = PhoneNumberField(
        default='',
        unique=True,
        validators=(
            phone_number_validator,
        ),
    )

    avatar = models.URLField()

    country = models.CharField(
        max_length=max(len(x) for (x, _) in COUNTRIES_CHOICES),
        choices=COUNTRIES_CHOICES,
    )

    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
        default='',
        validators=(
            MinLengthValidator(NAMES_MIN_LENGTH),
            only_letters_validator,
        ),
    )

    address = models.CharField(
        max_length=ADDRESS_MAX_LENGTH,
        default='',
        validators=(
            MinLengthValidator(ADDRESS_MIN_LENGTH),
        ),
    )

    def __str__(self):
        return f'{self.username} - {self.first_name} {self.last_name}'


class Product(models.Model):
    PRODUCT_MAX_LENGTH = 20
    PRODUCT_MIN_LENGTH = 3

    CATEGORIES = (
        "Bakery",
        "Fruit and Vegetables",
        "Meat and Fish",
        "Dairy",
        "Bio",
        "Special Foods",
        "Frozen Foods",
        "Drinks",
        "Cosmetics",
        "Home and Office supplies"
    )
    CATEGORIES_CHOICES = [(x, x) for x in CATEGORIES]

    product = models.CharField(
        max_length=PRODUCT_MAX_LENGTH,
        default='',
        validators=(
            MinLengthValidator(PRODUCT_MIN_LENGTH),
        ),
    )

    category = models.CharField(
        max_length=max(len(x) for (x, _) in CATEGORIES_CHOICES),
        choices=CATEGORIES_CHOICES,
    )

    quantity = models.IntegerField(
        default=1,
    )

    similar_products = models.ManyToManyField(
        'self',
        blank=True,
    )

    def get_similar_products(self):
        return Product.objects.filter(category=self.category).exclude(id=self.id)[:3]

    def __str__(self):
        return self.product
