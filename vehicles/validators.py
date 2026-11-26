from django.core.exceptions import ValidationError


def validate_brand(value: str) -> None:
    if len(value) == 0:
        raise ValidationError('Brand must not be empty')
    if not value[0].isupper():
        raise ValidationError('Brand must be capitalized')
