import string
import random

from view import View

import logging

logging.basicConfig(filename="leather-snake.log", encoding="utf-8", level=logging.INFO)


def random_letter():
    """Returns a random upper or lower case letter from the english alphabet"""
    return random.choice(string.ascii_letters)


def generate_text(length: int, _path: str) -> bool:
    """generates the letter A length times and writes to file

    Returns true on success.

    """
    logging.info("writing to file")
    with open(_path, "w") as _file:
        for _ in range(length):
            _file.write(random_letter())
            logging.info("writing letter")
        return True


if __name__ == "__main__":
    view = View()
    generate_text(view.args().file_length, view.args().file_path)
