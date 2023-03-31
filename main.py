import string
import random


def random_letter():
    """Returns a random upper or lower case letter from the english alphabet"""
    return random.choice(string.ascii_letters)


def generate_text(length: int, _path: str) -> bool:
    """generates the letter A length times and writes to file

    Returns true on success.

    """
    with open(_path, "w") as _file:
        for _ in range(length):
            _file.write(random_letter())
        return True


if __name__ == "__main__":
    generate_text(1200, "./temp_file.txt")
