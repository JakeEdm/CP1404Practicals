import random

MIN_NUMBER = 1
MAX_NUMBER = 46
NUMBERS_PER_LINE = 6


def main():
    total_quick_picks = int(input("How many quick picks? "))

    for pick in range(total_quick_picks):
        quick_picks = []
        for i in range(NUMBERS_PER_LINE):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_picks:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:2}".format(number) for number in quick_picks))


main()
