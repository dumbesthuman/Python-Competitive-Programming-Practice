# Experiment 2 - Final Order Cost with Multiple Discounts
# Source: Lab Sheet LO2

def calculate_final_cost(items):
    subtotal = 0

    # Apply item-level discounts
    for price, discount_percent in items:
        item_cost = price - (price * discount_percent / 100)
        subtotal += item_cost

    # Apply order-level discounts
    percentage_discount = 0
    fixed_discount = 0

    if subtotal > 500:
        percentage_discount = subtotal * 0.10

    if subtotal > 1000:
        fixed_discount = 150

    # Take maximum discount
    discount = max(percentage_discount, fixed_discount)

    final_cost = subtotal - discount
    return int(final_cost)


# Input
n = int(input())
items = []

for _ in range(n):
    price, discount = map(int, input().split())
    items.append((price, discount))

print("Final Cost:", calculate_final_cost(items))
