from taxi import Taxi


# CONSTANTS

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0.0):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.fanciness * Taxi.price_per_km

    def get_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)


