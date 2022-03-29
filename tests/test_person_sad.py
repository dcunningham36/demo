import pytest
from Person import Person

def test_run_return_false_hunger():
    p1 = Person("abc", 150, 50, 40)
    assert p1.run(26) == False

def test_run_return_false_energy():
    p1 = Person("abc", 150, 50, 40)
    assert p1.run(20) == False

def test_create_person_hunger_exception():
    with pytest.raises(Exception) as ex:
        p1 = Person("abc", 150, 101, 40)
    assert str(ex.value) == "Hunger must be between 0 and 100"