"""Guitars"""

from prac_06.guitar import Guitar


def main():
    """Add guitars to a list in class format"""
    # guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(guitars[-1], "added")
        name = input("Name: ")
    if len(guitars) > 0:
        print_guitars(guitars)


def print_guitars(guitars):
    """Displays all guitars stored"""
    print("These are my guitars:")
    spacing = max(len(guitar.name) for guitar in guitars)
    for i, guitar in enumerate(guitars, 1):
        response = "(Vintage)" if guitar.is_vintage() else ""
        print(f'Guitar {i}: {guitar.name:>{spacing}} ({guitar.year}), worth $ {guitar.cost:9,.2f} {response}')


main()
