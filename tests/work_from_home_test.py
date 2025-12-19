from src.kattis.work_from_home import expense_dollars

def test_expense_dollars():
    # Test case 1: normal usage
    assert expense_dollars(1000, 60, 10) == 1  # 1 kW * 1 hour * 10 cents = 10 cents → 1 dollar ceil
    assert expense_dollars(1500, 30, 20) == 1  # 1.5 kW * 0.5 hr * 20 = 15 cents → 1 dollar ceil
    assert expense_dollars(2000, 120, 50) == 100  # 2 kW * 2 hr * 50 = 200 cents → 2 dollars ceil
    # Test zero consumption
    assert expense_dollars(0, 60, 10) == 0
    # Test very small usage
    assert expense_dollars(1, 1, 1) == 1  # ceil(1/100) = 1
