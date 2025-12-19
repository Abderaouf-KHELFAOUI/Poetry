from src.kattis.puzzle import solve_puzzle


def test_solve_puzzle():

    tests = [
        ("123-", 0),
        ("1-23", 1),
        ("-123", 2),
        ("213-", 3),
        ("3-21", 4),
    ]

    for s, answer in tests:
        assert solve_puzzle(s) == answer
