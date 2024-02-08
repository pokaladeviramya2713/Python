import re

def is_valid_number(s):
    # Regular expression to match valid number patterns
    pattern = r'^[+-]?(\d+\.\d*|\.\d+|\d+)([eE][+-]?\d+)?$'
    
    return bool(re.match(pattern, s))

# Test cases
print(is_valid_number("0"))    # Output: True
print(is_valid_number("e"))    # Output: False
print(is_valid_number("s"))    # Output: False
print(is_valid_number(""))      # Output: False
print(is_valid_number("%"))     # Output: False
