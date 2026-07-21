def password_checker(password):
    """
    Sprawdza czy hasło:
    - ma co najmniej 8 znaków
    - zawiera przynajmniej jedną małą literę
    - zawiera przynajmniej jedną wielką literę
    - zawiera przynajmniej jedną cyfrę
    """

    if len(password) < 8:
        return False

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_lower and has_upper and has_digit
