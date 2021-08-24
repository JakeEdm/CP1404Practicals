"""Module docstring"""


# imports
# CONSTANTS

def main():
    """Function docstring"""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username = input("Username: ")
    while username not in usernames:
        print("Access Denied")
        username = input("Username: ")
    print("Access Granted")

    numbers = []
    total_numbers = int(input("How many numbers? "))
    for number in range(total_numbers):
        number = int(input("Number: "))
        numbers.append(number)

    display_information(numbers)


def display_information(numbers):
    print(f"The first number is {numbers[0]}")
    print(f'The last number is {numbers[-1]}')
    print(f'The smallest number is {min(numbers)}')
    print(f'The largest number is {max(numbers)}')
    print(f'The average of the numbers is {sum(numbers) / len(numbers)}')


def do_stuff():
    """Function docstring"""
    # statements...  


main()
