import pytest
from fuel import convert, gauge

def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_valueerror():
    with pytest.raises(ValueError):
        convert("7/5")
    with pytest.raises(ValueError):
        convert("-3/5")
    with pytest.raises(ValueError):
        convert("4/-3")

def test_EF():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(65) == "65%"

def test_convert_basic():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75

def test_convert_edges():
    assert convert("0/1") == 0
    assert convert("1/1") == 100