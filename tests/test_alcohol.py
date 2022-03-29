import pytest
import alcohol

def test_person_looks_over_25():
    assert alcohol.canBuyAlcohol(True) == True

def test_no_id_no_sale():
    assert alcohol.canBuyAlcohol(False) == False

def test_too_young_to_buy_alcohol():
    assert alcohol.canBuyAlcohol(False, 17) == False

def test_id_check_can_buy_alcohol():
    assert alcohol.canBuyAlcohol(False, 18) == True