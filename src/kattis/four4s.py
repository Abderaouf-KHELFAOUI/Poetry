# Problem: Four Fours
# URL: https://open.kattis.com/problems/fourfours
#
# Find a mathematical expression using exactly four 4's and three binary
# operations (+, -, *, /) that evaluates to a target number.

def evaluate(a, op1, b, op2, c, op3, d):
    # build expression respecting operator precedence
    expr = f"{a} {op1} {b} {op2} {c} {op3} {d}"
    
    # evaluate manually with correct precedence
    ops = [op1, op2, op3]
    vals = [a, b, c, d]
    
    # first pass: handle * and /
    i = 0
    while i < len(ops):
        if ops[i] == '*':
            vals[i] = vals[i] * vals[i + 1]
            vals.pop(i + 1)
            ops.pop(i)
        elif ops[i] == '/':
            if vals[i + 1] == 0:
                return None, None
            vals[i] = int(vals[i] / vals[i + 1])
            vals.pop(i + 1)
            ops.pop(i)
        else:
            i += 1
    
    # second pass: handle + and -
    result = vals[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += vals[i + 1]
        else:
            result -= vals[i + 1]
    
    return result, expr

def find_solution(target):
    operations = ['+', '-', '*', '/']
    
    for op1 in operations:
        for op2 in operations:
            for op3 in operations:
                result, expr = evaluate(4, op1, 4, op2, 4, op3, 4)
                if result == target:
                    return expr + f" = {target}"
    
    return "no solution"