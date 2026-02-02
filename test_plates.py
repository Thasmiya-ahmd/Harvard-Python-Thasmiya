import pytest
from plates import is_valid

def test_valid_length():
    assert is_valid("Hello")==True
    assert is_valid("50")==False

def test_valid_two_alpha():
    assert is_valid("Hell78")==True
    assert is_valid("a50")==False

def test_valid_special():
    assert is_valid("He,l78")==False
    assert is_valid("a5 0")==False

def test_valid_ends_num():
    assert is_valid("Hell78")==True
    assert is_valid("a50b")==False
