import pytest
from Person import Person

@pytest.fixture
def default_person():
    print("Before")
    yield Person("abc", 150, 50, 40)
    print("After")