from twttr import shorten

def test_helloworld():
    assert shorten("Hello, world") == "Hll, wrld"
    assert shorten("My name is Eliza") == "My nm s lz"

def test_thisisCS50():
    assert shorten("This is CS50") == "Ths s CS50"

def test_uppercasevvowels():
    assert shorten("HELLO, WORLD") == "HLL, WRLD"