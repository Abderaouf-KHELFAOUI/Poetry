# Electricity Expense Calculator
# https://open.kattis.com/problems/workfromhome
#


import math

def expense_dollars(W, M, C):
    # Convert watts to kilowatts
    kW = W / 1000.0

    # Convert minutes to hours
    hours = M / 60.0

    # Energy in kWh
    kWh = kW * hours

    # Cost in cents
    cost_cents = kWh * C

    # Convert to dollars and round up
    return math.ceil(cost_cents / 100.0)
