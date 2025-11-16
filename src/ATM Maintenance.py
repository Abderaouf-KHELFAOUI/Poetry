# ATM Queue Simulation
# https://open.kattis.com/problems/atm2
#
# Given the initial amount in the ATM and the withdrawals requested,
# determine for each person whether their withdrawal succeeds.

def atm_withdrawals(total, requests):
    result = []

    for amount in requests:
        if amount <= total:
            result.append('1')
            total -= amount
        else:
            result.append('0')

    return "".join(result)