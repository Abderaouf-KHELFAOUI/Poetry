from src.kattis.wordsfornumbers import numbers_to_words


def test_conversion():

    lines = [
        "I have 3 dogs",
        "42 is the answer",
        "100 bottles of milk",
        "9999 soldiers marching",
    ]

    for line in lines:
        result = numbers_to_words(line)
        assert isinstance(result, str)
        assert line != result
