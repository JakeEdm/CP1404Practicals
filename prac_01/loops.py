for i in range(1, 21, 2):
    print(i, end=' ')
print()

# A

for i in range(0, 100, 10):
    print(i, end=" ")
print()

# B

for i in range(20, 0, -1):
    print(i, end=" ")
print()

# C

number = int(input("Enter Number: "))

for i in range(number):
    print("*", end="")
print()

# D

number = int(input("Enter Number: "))

for i in range(1, number + 1):
    print("*" * i)
print()


