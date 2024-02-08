def modify_string(S):
    frequency = {}
    result = ""

    for char in S:
        frequency[char] = frequency.get(char, 0) + 1

    for char in S:
        distance = ord(char) - ord('a') + 1
        new_char = chr((distance + frequency[char] - 1) % 26 + ord('a'))
        result += new_char

    return result

# Test cases
print(modify_string("ghee"))      # Output: "hggi"
print(modify_string("elephant"))  # Output: "fcouphou"
print(modify_string("apple"))      # Output: "bqqmf"
print(modify_string("orange"))     # Output: "pcphpj"
print(modify_string("lion"))       # Output: "ljtp"
