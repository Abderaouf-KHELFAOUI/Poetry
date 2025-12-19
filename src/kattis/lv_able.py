# https://open.kattis.com/problems/lvable
# Returns minimum operations to make string contain "lv"

def solve(n, s):
    s = s.strip()  # remove leading/trailing whitespace
    if "lv" in s:
        return 0

    for i in range(n):
        for j in range(i + 1, n + 1):
            temp = s[:i] + s[i:j][::-1] + s[j:]
            if "lv" in temp:
                return 1

    if 'l' in s or 'v' in s:
        return 1

    return 1 if n >= 2 else 2

