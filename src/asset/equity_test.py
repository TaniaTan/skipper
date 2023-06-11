import pytest
from .equity import Equity

def test_security():
    equity = Equity(name="AAPL")
    assert(equity.getName() == "AAPL")
