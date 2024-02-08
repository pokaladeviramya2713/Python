def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_num = 0
    original_x = x

    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10

    return original_x == reversed_num

# Test Cases
print(isPalindrome(121))   # Output: True
print(isPalindrome(-121))  # Output: False
print(isPalindrome(10))    # Output: False

