
class Bridge:

    def __init__(self, max_weight):
        self.vehicles = []
        self.max_weight = max_weight

    def calc_total_weight(self):
        total = 0.0
        for v in self.vehicles:
            total += v.weight
        return total


    def add_vehicle(self, veh):

        if self.calc_total_weight() + veh.weight <= self.max_weight:
            self.vehicles.append(veh)
            return True

        return False
