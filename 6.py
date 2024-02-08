def max_area(height):
    max_area_result = 0
    left, right = 0, len(height) - 1

    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_area_result = max(max_area_result, h * w)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area_result

# Test Cases
print(max_area([1, 5, 4, 3]))                  # Output: 6
print(max_area([3, 1, 2, 4, 5]))               # Output: 12
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))   # Output: 49
print(max_area([1, 1]))                        # Output: 1
print(max_area([1, 7, 3]))                     # Output: 3
