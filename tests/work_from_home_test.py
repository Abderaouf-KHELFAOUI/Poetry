from kattis.work_from_home import numbers_to_words


def test_numbers_to_words():

    lines = [
        "I have 3 dogs",
        "42 is the answer",
        "100 bottles of milk",
        "9999 soldiers marching",
    ]

    for line in lines:
        converted = numbers_to_words(line)

        # output must be a string
        assert isinstance(converted, str)

        # must not return None
        assert converted is not None

        # must change at least one word
        assert converted != line
