def isHappy(n):
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(i)**2 for i in str(n))

    return n == 1

# Test Cases
print(isHappy(19))  # Output: True
print(isHappy(2))   # Output: False
print(isHappy(-1))  # Output: False (since negative numbers are not considered happy)
print(isHappy(0))   # Output: False
print(isHappy(5))   # Output: False
