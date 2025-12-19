# tests/test_lv_able.py
from src.kattis.lv_able import solve  # import your function

def test_already_contains_lv():
    assert solve(4, "love") == 1
    assert solve(2, "lv") == 1

def test_single_reverse_needed():
    # "vl" can be reversed to "lv"
    assert solve(2, "vl") == 1
    # "lxxv" can reverse "xxv" to get "lv"
    assert solve(4, "lxxv") == 1

def test_has_l_or_v():
    # has 'l' but no 'v', can do 1 operation
    assert solve(3, "lxx") == 1
    # has 'v' but no 'l', can do 1 operation
    assert solve(3, "vxx") == 1

def test_needs_insertion():
    # no 'l' or 'v', small strings
    assert solve(1, "a") == 2
    # string longer than 2 but no 'l' or 'v'
    assert solve(3, "abc") == 1
