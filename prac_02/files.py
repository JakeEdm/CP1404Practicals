# # 1.
#
# out_file = open('name.txt', "w")
#
# name = input("What is your name: ")
#
# print(name, file=out_file)
#
# out_file.close()
#
# # 2.
#
# in_file = open('name.txt', 'r')
#
# name = in_file.read()
#
# print(f'Your name is {name}')
#
# in_file.close()

# 3.

# in_file = open('numbers.txt', 'r')
#
# line1 = int(in_file.readline())
# line2 = int(in_file.readline())
#
# print(line1 + line2)
#
# in_file.close()

# 4.

in_file = open('numbers.txt', 'r')

total = 0
for line in in_file:
    total += int(line)

print(total)

in_file.close()