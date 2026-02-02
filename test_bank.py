import pytest
from bank import value

def test_hello():
    assert value("hello")=="$0"

def test_hey():
    assert value("heyy")=="$20"

def test_remain():
    assert value("what are you doing")=="$100"