"""
Custom validators
"""
import phonenumbers

from django.core.exceptions import ValidationError

PHONE_NUMBER_REGIONS = {'BG', 'CN', 'NL'}


def only_letters_validator(value):
    if not all(char.isalpha() for char in value):
        raise ValidationError("Value must consist only of letters!")


def phone_number_validator():
    def validate(value):
        for region in PHONE_NUMBER_REGIONS:
            try:
                full_length_number = phonenumbers.parse(value, region)
                if phonenumbers.is_valid_number(full_length_number):
                    return None
            except phonenumbers.NumberParseException:
                continue

        raise ValidationError("Invalid phone number!")

    return validate
