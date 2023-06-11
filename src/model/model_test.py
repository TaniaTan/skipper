import pytest
from .model import Model
from .sector import Sector

def buildSP500Model():
    """
    Build a mini version of sp500 model. 
    full model sepc: https://www.sofi.com/learn/content/sp-500-sectors/
    """
    sp500 = Model("SP500")
    root = sp500.GetRoot()
    """Tech """
    tech_sector = Sector("Technology")
    root.addSector(tech_sector)
    software_service = Sector("Software & Service")
    tech_sector.addSector(software_service)
    it_service = Sector("IT Services")
    software_service.addSector(it_service)
    software = Sector("Software")
    software_service.addSector(software)

    """Financial"""
    financial_sector = Sector("Financials")
    root.addSector(financial_sector)
    bank = Sector("Banks")
    financial_sector.addSector(bank)
    bank_sub = Sector("Banks")
    bank.addSector(bank_sub)

    financial_service = Sector("Financial Services")
    financial_sector.addSector(financial_service)
    financial_service_sub = Sector("Financial Services")
    financial_service.addSector(financial_service_sub)
    consumer_finance = Sector("Consumer Finance")
    financial_service.addSector(consumer_finance)
    capitial_market = Sector("Capital Markets")
    financial_service.addSector(capitial_market)
    reits = Sector("Mortgage Real Estate Investment Trusts (REITs)")
    financial_service.addSector(reits)
    return sp500
def test_model():
    model = Model("SP500")
    assert str(model) == "Model: SP500"

def test_getAllLeaves():
    sp500 = buildSP500Model()
    leaves = sp500.GetAllLeaves()
    leaves_names = sorted([str(i) for i in leaves])
    expected_result = sorted(["IT Services", "Software", "Banks", "Financial Services", "Consumer Finance", "Capital Markets","Mortgage Real Estate Investment Trusts (REITs)"])
    assert leaves_names == expected_result