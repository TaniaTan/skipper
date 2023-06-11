import pytest
from .security import Security

def test_security():
    security = Security()
    assert(security.getName() == None)

