import pytest
from .bond import Bond

def test_security():
    bond = Bond(name="AAPL", date = "01/40")
    assert(bond.getName() == "AAPL 01/40")
