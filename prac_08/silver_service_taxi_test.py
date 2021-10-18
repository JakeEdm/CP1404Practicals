from silver_sevice_taxi import SilverServiceTaxi


# CONSTANTS

def main():
    """Function docstring"""
    taxi = SilverServiceTaxi("Hummer", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(f'${taxi.get_fare()}')
    # taxi.start_fare()
    # taxi.drive(66)
    # print(f'${taxi.get_fare()}')


main()
