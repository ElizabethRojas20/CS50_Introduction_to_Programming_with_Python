from bank import value

def test_uppercase():
    assert value("HELLO world") == "$0"
    assert value("Hello") == "$0"
    assert value("HII") == "$20"
    assert value("Hi hi hi") == "$20"
    assert value("MY NAME IS ELI") == "$100"
    assert value("Nice to meet you") == "$100"

def test_lowercase():
    assert value("hELLO world") == "$0"
    assert value("hello") == "$0"
    assert value("hII") == "$20"
    assert value("hi hi hi") == "$20"
    assert value("my name is eli") == "$100"
    assert value("nice to meet you") == "$100"

def test_punctuations():
    assert value("Hello, WORLD") == "$0"
    assert value("Hi, world") == "$20"
    assert value("My name is eli, nice to meet you") == "$100"

def test_common():
    assert value("Ahello") == "$100"