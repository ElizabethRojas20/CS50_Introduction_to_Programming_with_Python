from plates import is_valid

def test_long():
    assert is_valid("CS5043GRSFR123235") == False
    assert is_valid("CS584HFR33920DFDADF") == False

def test_short():
    assert is_valid("C") == False
    assert is_valid("S") == False

def test_numbers():
    assert is_valid("13434") == False
    assert is_valid("35254") == False
    assert is_valid("CS50P2") == False

def test_valid_ones():
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True

def test_zero():
    assert is_valid("CS05") == False

def test_alphanumeric():
    assert is_valid("CS.50") == False
    assert is_valid("PI3.14") == False
