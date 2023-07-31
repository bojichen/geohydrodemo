import random
import string

def random_string(string_length = 3):
    """Generate a random string of fixed length.

    Args:
        string_length (int, optional): Fixed length. Defaults to 3.

    Returns:
        str: A random string
    """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(string_length))