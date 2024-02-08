def count_sorted_vowel_strings(n):
    dp = [[0] * 5 for _ in range(n)]
    
    for i in range(5):
        dp[0][i] = 1
    
    for i in range(1, n):
        for j in range(5):
            dp[i][j] = sum(dp[i - 1][k] for k in range(j + 1))
    
    return sum(dp[n - 1])

# Test cases
print(count_sorted_vowel_strings(1))  # Output: 5
print(count_sorted_vowel_strings(2))  # Output: 15
print(count_sorted_vowel_strings(33))  # Output: 66045
