"""Quick Picks"""


import random


quick_picks = int(input("How many Quick Picks? "))
for pick in range(quick_picks):
    print()
    for number in range(6):
        print(random.randint(1, 45), end="")
