import pytest
from twttr import shorten

def test_vowels():
    assert shorten("thasmiya")=="thsmy"
    assert shorten("What Is your Name?")=="Wht s yr Nm?"
    assert shorten("CS50")=="CS50"