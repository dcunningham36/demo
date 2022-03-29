from Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, reg, weight):
        super().__init__(reg, weight)

    def calculate_fee(self):
        if self.weight < 1590:
            return 5.00

        diff = self.weight - 1590

        extra = int(diff/100) * 0.1

        return 5.0 + extra
