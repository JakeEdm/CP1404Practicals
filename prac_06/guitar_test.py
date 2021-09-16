"""Module docstring"""

from prac_06.guitar import Guitar


def main():
    """Function docstring"""
    ibanez = Guitar("Ibanez S671ALB BCM", 2005, 2124.40)
    lez_paul = Guitar("Gibson Les Paul Classic", 1966, 3556.54)
    guitars = [ibanez, lez_paul]
    for guitar in guitars:
        print("The {} is {} years old".format(guitar.name, guitar.get_age()))

    print("16-year old guitar is_vintage() - Expected False. Got", Guitar.is_vintage(ibanez))

main()
