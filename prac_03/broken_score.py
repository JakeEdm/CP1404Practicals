"""
CP1404/CP5632 - Practical
Broken Score
"""

import random


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(calculate_grade(score))

    score = random.randint(0, 101)
    print(f'A score of {score} is {calculate_grade(score)}')


def calculate_grade(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
