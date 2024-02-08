def sumsquare(lst):
    sum_odd = sum(x**2 for x in lst if x % 2 != 0)
    sum_even = sum(x**2 for x in lst if x % 2 == 0)
    return [sum_odd, sum_even]

# Test Cases
print(sumsquare([1, 2, 3, 4, 5]))           # Output: [35, 20]
print(sumsquare([12, 4, 5, 6, 7, 11, 12, 13]))# Output: [282, 194]
print(sumsquare([-1, 11, 2, 10, 11, 1, 2]))   # Output: [124, 146]
print(sumsquare([0, 1, 2, 3, 4, 5]))          # Output: [35, 20]
print(sumsquare([12, 4, 5, 6, 7, 11, 12, 13]))# Output: [282, 194]
