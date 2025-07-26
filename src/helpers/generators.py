import random
import string


def generate_login(domain: str = "example.com") -> str:
    """
    Generate a random username in the format <letters><digits>@<domain>.
    """
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(6))
    digits = random.randint(1000, 9999)
    return f"{letters}{digits}@{domain}"


def generate_password(length: int = 10) -> str:
    """
    Generate a random password of given length, including letters and digits.
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
