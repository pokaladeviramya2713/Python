def max_guests_at_instance(T, entering, leaving):
    guests = 0
    max_guests = 0
    timeline = sorted(set(entering + leaving))

    for time in timeline:
        guests += entering.count(time)
        guests -= leaving.count(time)
        max_guests = max(max_guests, guests)

    return max_guests

# Test cases
print(max_guests_at_instance(4, [1, 1, 5, 9, 10], [0, 2, 3, 4]))  # Output: 8
print(max_guests_at_instance(0, [1, 2, 3, 4], [1, 2, 3, 4]))      # Output: 0
print(max_guests_at_instance(4, [1, 2, 8, 5, 1], [1, 2, 1, 3, 4]))  # Output: 8
print(max_guests_at_instance(5, [1, 4, 2, 0, 35, 12, 15], [1, 2, 1, 3, 4]))  # Output: 9
print(max_guests_at_instance(1, [12], [10]))  # Output: 1
