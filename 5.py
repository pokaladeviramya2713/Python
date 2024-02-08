# Get input from the user
fresh_loaves = int(input("Enter the number of fresh loaves purchased: "))
day_old_loaves = int(input("Enter the number of day-old loaves purchased: "))

# Constants
regular_price = 185
discount_percentage = 60

# Calculate prices
regular_cost = fresh_loaves * regular_price
discounted_cost = day_old_loaves * (regular_price * (100 - discount_percentage) / 100)
total_cost = regular_cost + discounted_cost

# Display the results with two decimal places
print(f"Regular price: Rs.{regular_cost:.2f}")
print(f"Amount of new loaves: Rs.{regular_cost:.2f}")
print(f"Amount of day-old loaves: Rs.{discounted_cost:.2f}")
print(f"Total amount: Rs.{total_cost:.2f}")
