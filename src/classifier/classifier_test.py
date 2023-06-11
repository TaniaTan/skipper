import pytest 
from src.asset.equity import Equity
from src.asset.bond import Bond
from src.model.sector import Sector
from src.model.model import Model
from .classifier import Classifier

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

def buildTestSecurities():
    rst = []
    apple = Equity("AAPL")
    apple.setColumnValue("sp500", "Software")
    rst.append(apple)
    google = Equity("GOOG")
    google.setColumnValue("sp500", "IT Services")
    rst.append(google)
    gs = Equity("GS")
    gs.setColumnValue("sp500", "Banks")
    rst.append(gs)
    apple_bond = Bond("AAPL", "01/40")
    apple_bond.setColumnValue("sp500", "Software")
    rst.append(apple_bond)

    return rst

def test_classification():
    sp500 = buildSP500Model()
    classifier = Classifier("sp500", sp500)
    securities = buildTestSecurities()
    rst = classifier.classification(
        securities
    )
    except_result = {
        "AAPL": "SP500/Technology/Software & Service/Software",
        "GOOG": "SP500/Technology/Software & Service/IT Services",
        "GS" : "SP500/Financials/Banks/Banks",
        "AAPL 01/40": "SP500/Technology/Software & Service/Software",
    }
    converted_result = {str(k): v.getPath() for k, v in rst.items()}
    assert except_result == converted_result