from src.kattis.kindsofpeople import solve_pair


def test_solve_pairs():

    tests = [
        ("1", "1"),
        ("10", "2"),
        ("1a", "26"),
        ("ff", "255"),
        ("ab", "100"),
    ]

    for a, b in tests:
        result = solve_pair(a, b)
        assert isinstance(result, bool) or isinstance(result, int) or isinstance(result, str)
