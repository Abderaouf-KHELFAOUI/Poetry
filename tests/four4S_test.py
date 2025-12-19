from src.kattis.four4s import find_solution


def test_find_solution_range():

    for x in range(-5, 21):
        result = find_solution(x)
        assert isinstance(result, str)
