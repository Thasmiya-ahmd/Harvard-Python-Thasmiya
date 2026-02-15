from jar import jar
import pytest

def test_init():
    j=jar()
    with pytest.raises(ValueError):
        jar(-1)
def test_str():
    j=jar()
    assert str(j)==""
    j.deposit(5)
    assert str(j)=="🍪🍪🍪🍪🍪"
    j.withdraw(2)
    assert str(j)=="🍪🍪🍪"
def test_deposit():
    j=jar()
    j.deposit(5)
    assert str(j)=="🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        j.deposit(8)
def test_withdraw():
    j=jar()
    j.deposit(12)
    j.withdraw(5)
    assert str(j)=="🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        j.withdraw(12)