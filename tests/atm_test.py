from src.kattis.ATM import atm_withdrawals


def test_atm_withdrawals():

    total = 100
    requests = [20, 40, 50, 10, 30]

    expected = [1, 1, 0, 1, 0]  # from your print script

    assert atm_withdrawals(total, requests) == expected
