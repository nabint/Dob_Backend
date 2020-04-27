from django.core.exceptions import ValidationError

def name_validator(value):
    print("Name Validators Called")
    if not "on" in value:
        print("Value is null")
        return ValidationError("Name must not be null")
    else:
        return value