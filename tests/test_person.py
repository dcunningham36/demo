import pytest
from Person import Person

def setup_function(function):
    global p1
    p1 = Person("abc", 150, 50, 40)

def test_create_person(default_person):
    assert default_person.name == "abc"
    assert default_person.weight == 150

def test_run_energy_changes():
    p1.run(5)
    assert p1.energy == 30

def test_run_hunger_changes(default_person):
    default_person.run(5)
    assert default_person.hunger == 60

def test_run_returns_true():
    assert p1.run(5) == True