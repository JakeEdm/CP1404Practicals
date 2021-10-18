"""Module docstring"""
from taxi import Taxi
from silver_sevice_taxi import SilverServiceTaxi

# CONSTANTS
MENU = """(Q)uit
(C)hoose
(D)rive"""


def main():
    """Function docstring"""
    current_taxi = None
    lifetime_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 150, 5)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxi's Available")
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif choice == "D":
            if current_taxi:
                current_taxi.start_fare()
                distance = int(input("How far do you want to travel? "))
                current_taxi.drive(distance)
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
                lifetime_bill += current_taxi.get_fare()
            else:
                print("Please select a taxi first")
        else:
            print("Invalid choice")
        print(f"Bill to date: ${lifetime_bill:.2f}")
        print(MENU)
        choice = input(">>>").upper()


def display_taxis(taxis):
    count = 0
    for taxi in taxis:
        print(f"{count} - {taxi.__str__()}")
        count += 1


def choose_taxi(taxis):
    taxi_number = int(input("Choose Taxi: "))
    try:
        taxi = taxis[taxi_number]
        return taxi
    except IndexError:
        print("Invalid choice")


main()
