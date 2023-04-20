from main import random_letter


def test_random_letter_generates_random_letter():
    assert random_letter() is not None


def test_bogus():
    assert True == False
