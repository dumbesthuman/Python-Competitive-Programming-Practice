#Problem: Tiered Discount Calculator
#Category: Basics / Conditional Logic
#Source: Lab Sheet LO1

#Approach:
#- Use if-else ladder
#- Apply discount based on range

#Time Complexity: O(1)
#Space Complexity: O(1)


amount = int(input())

if amount < 1000:
    final_amount = amount
elif amount < 5000:
    final_amount = amount - (amount * 0.10)
elif amount < 10000:
    final_amount = amount - (amount * 0.20)
else:
    final_amount = amount - (amount * 0.25) - 500

print("Final amount to be paid:", int(final_amount))
