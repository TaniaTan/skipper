from .sector import Sector
from src.asset.equity import Equity
import pytest

def test_SubSector():
    equity = Equity('TEST')
    with pytest.raises(Exception):
        sector = Sector("it")
        sub_sector = Sector("ads")
        sector.addSector(sub_sector)
        sector.addSecurity(equity)

def test_securitySectorCannotAddSubSector():
    equity = Equity('TEST')
    with pytest.raises(Exception):
        sector = Sector("it")
        sub_sector = Sector("ads")
        sector.addSecurity(equity)
        sector.addSector(sub_sector)

def test_recursiveGetSecurities():
    apple = Equity("AAPL")
    IBM = Equity("IBM")
    Goog = Equity("GOOG")
    it_sector = Sector("IT")
    ads_sector = Sector("ADS")
    hdw_sector = Sector("HARDWARE")
    it_sector.addSector(ads_sector)
    it_sector.addSector(hdw_sector)
    ads_sector.addSecurity(Goog)
    hdw_sector.addSecurity(IBM)
    hdw_sector.addSecurity(apple)
    rst = it_sector.getSecurities()
    rst.sort()
    assert(rst == sorted([apple, IBM, Goog]))


def test_getPath():
    it_sector = Sector("IT")
    ads_sector = Sector("ADS")
    hdw_sector = Sector("HARDWARE")
    it_sector.addSector(ads_sector)
    it_sector.addSector(hdw_sector)
    ads_sector.setParent(it_sector)
    hdw_sector.setParent(it_sector)
    assert hdw_sector.getPath() == "IT/HARDWARE"
    assert ads_sector.getPath() == "IT/ADS"