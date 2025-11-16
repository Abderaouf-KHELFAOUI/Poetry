# https://open.kattis.com/problems/lvable
# Returns minimum operations to make string contain "lv"

def solve(n, s):
    if "lv" in s:
        return 0
    
    # check all reverses
    for i in range(n):
        for j in range(i + 1, n + 1):
            temp = s[:i] + s[i:j][::-1] + s[j:]
            if "lv" in temp:
                return 1
    
    # we can always do it in 1 op if we have l or v
    if 'l' in s or 'v' in s:
        return 1
    
    # otherwise replace 2 chars or insert both
    return 1 if n >= 2 else 2
