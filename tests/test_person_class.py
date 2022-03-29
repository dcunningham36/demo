import pytest
from Person import Person

class TestPerson:

    def setup_method(self, method):
        self.p1 = Person("abc", 150, 99, 1)

    def test_rest_energy_changes(self):
        self.p1.rest()
        assert self.p1.energy == 2

    def test_rest_hunger_changes(self):
        self.p1.rest()
        assert self.p1.hunger == 100