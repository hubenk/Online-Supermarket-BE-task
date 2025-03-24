from django import forms
from django.core.exceptions import ValidationError

from .models import UserProfile
from .models import (
    FIRST_NAME_MAX_LENGTH,
    LAST_NAME_MAX_LENGTH,
    USER_MAX_LENGTH,
    EMAIL_MAX_LENGTH,
    PHONE_NUMBER_MAX_LENGTH,
    CITY_MAX_LENGTH,
    ADDRESS_MAX_LENGTH,
    NAMES_MIN_LENGTH,
    ADDRESS_MIN_LENGTH
)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'avatar',
            'country',
            'city',
            'address'
        ]

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < NAMES_MIN_LENGTH or len(first_name) > FIRST_NAME_MAX_LENGTH:
            raise ValidationError(f"First name must be between {NAMES_MIN_LENGTH} "
                                  f"and {FIRST_NAME_MAX_LENGTH}")
        return first_name

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
