"""Convert character to Ascii"""
#
LOWER_BOUND = 33
UPPER_BOUND = 127
#
#
# character = input("What is your character?: ")
#
# print(f'The ASCII code for {character} is {ord(character)}')
#
# number = int(input("Enter a number: "))
# while number < LOWER_BOUND or number > UPPER_BOUND:
#     print('Number must be between {} and {}'.format(LOWER_BOUND, UPPER_BOUND))
#     number = int(input("Enter a number: "))
#
# print('The character for {} is {}'.format(number, chr(number)))
# print()

# columns = int(input("How many columns? "))
#
# for row in range():
#     for columns in range(columns):
#         print(f'{row:>3} {chr(row):>2}')



"""
CP1404/CP5632 - Practical - Suggested Solution
ASCII table and converter
"""
MAX_COLUMNS = 10
MIN_COLUMNS = 2

LOWER = 33
UPPER = 127



columns = int(input("Enter number of columns: "))
# calculate the range of values and the number of full rows
number_of_values = UPPER - LOWER + 1
rows = number_of_values // columns


print("Version 2: Vertical then horizontal ordering")
# iterate through rows
for row in range(rows + 1):
    starting_value = LOWER + row
    value = starting_value
    # print all column values not including the last one (-1)
    for column in range(columns - 1):
        value_to_print = value + (column * rows)
        print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
        value += 1

    # last column may not exist so handle separately
    # having the if statement outside the for loop means we don't do it every column
    # so it is more efficient (we can't avoid doing it every row AFAIK)
    value_to_print = value + ((column + 1) * rows)
    if value_to_print <= UPPER:
        print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
    print()
