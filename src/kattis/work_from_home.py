# Electricity Expense Calculator
# https://open.kattis.com/problems/workfromhome
#


import math

def expense_dollars(w, m, c):
    # Convert watts to kilowatts
    kW = w / 1000.0

    # Convert minutes to hours
    hours = m / 60.0

    # Energy in kWh
    kWh = kW * hours

    # Cost in cents
    cost_cents = kWh * c

    # Convert to dollars and round up
    return math.ceil(cost_cents / 100.0)

#
