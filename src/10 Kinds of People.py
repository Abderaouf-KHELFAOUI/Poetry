# Problem: Ten Kinds of People (Base Conversion)
# URL: https://open.kattis.com/problems/tenkindsofpeople
# 
# Given two numbers in unknown bases, find bases b1 and b2 such that
# when the numbers are interpreted in those bases, they have equal decimal values.
# Valid bases range from 2 to 7500.

def char_to_val(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    elif 'a' <= c <= 'z':
        return ord(c) - ord('a') + 10
    else:
        return ord(c) - ord('A') + 36

def to_decimal(num_str, base):
    result = 0
    for c in num_str:
        result = result * base + char_to_val(c)
    return result

def min_base(num_str):
    # minimum valid base is 1 + the largest digit value
    max_digit = 0
    for c in num_str:
        max_digit = max(max_digit, char_to_val(c))
    return max_digit + 1

def solve_pair(n1, n2):
    min_b1 = min_base(n1)
    min_b2 = min_base(n2)
    
    # try all combinations of bases
    for b1 in range(min_b1, 7501):
        v1 = to_decimal(n1, b1)
        if v1 > 10**15:  # prevent overflow
            break
        
        for b2 in range(min_b2, 7501):
            v2 = to_decimal(n2, b2)
            if v2 > 10**15:
                break
            
            if v1 == v2:
                return f"{v1} {b1} {b2}"
    
    return "CANNOT MAKE EQUAL"