
total_cost = 0

total_items = int(input("How many items are there? "))
while total_items < 0:
    print("Invalid number of items!")
    total_items = int(input("How many items are there? "))

for i in range(total_items):
    price = float(input("Price: "))
    total_cost += price

print(f"Total price for {total_items} items is ${total_cost:.2f}")

