from taxi import Taxi


# CONSTANTS

def main():
    """Test of the Taxi class"""
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi)
    print(f"${taxi.get_fare():.2f}")
    taxi.start_fare()
    taxi.drive(100)
    taxi.add_fuel(300)
    print(taxi)
    print(f"${taxi.get_fare():.2f}")


main()
