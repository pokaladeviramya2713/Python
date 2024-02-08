def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    mapping_s_t = {}
    mapping_t_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in mapping_s_t:
            if mapping_s_t[char_s] != char_t:
                return False
        else:
            mapping_s_t[char_s] = char_t

        if char_t in mapping_t_s:
            if mapping_t_s[char_t] != char_s:
                return False
        else:
            mapping_t_s[char_t] = char_s

    return True

# Test Cases
print(isIsomorphic("egg", "add"))      # Output: true
print(isIsomorphic("foo", "bar"))      # Output: false
print(isIsomorphic("paper", "title"))  # Output: true
print(isIsomorphic("fry", "sky"))      # Output: true
print(isIsomorphic("apples", "apple")) # Output: false
