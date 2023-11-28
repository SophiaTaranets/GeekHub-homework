import re


class ValidationException(Exception):
    pass


class BanknoteException(Exception):
    pass


class Validation:

    @staticmethod
    def validate_password(password):
        if not len(password) >= 5:
            raise ValidationException('Password must consist at least 5 symbols')

        # if not (any([symbol.isdigit() for symbol in password])):
        #     raise ValidationException('Password must consist at least 1 digit symbol')
        return password

    @staticmethod
    def validate_username(username):
        special_characters_pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
        if not len(username) in range(3, 51):
            raise ValidationException('User name consist symbols in range in 3 to 50')

        if special_characters_pattern.search(username):
            raise ValidationException('Username can`t consist special symbols')
        return username

    @staticmethod
    def validate_amount(amount_str):
        try:
            amount = float(amount_str)
            if amount < 0:
                raise ValidationException('Amount must be a positive number.')
        except ValueError:
            raise ValidationException('Amount must be a valid number.')

        return amount

    @staticmethod
    def validate_nominal(nominal):
        if int(nominal) not in [10, 20, 50, 100, 200, 500, 1000]:
            raise ValidationException(f'Available nominal: (10, 20, 50, 100, 200, 500, 1000)')
        return int(nominal)
