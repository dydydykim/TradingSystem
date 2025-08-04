import pytest

from auto_trading_system import AutoTradingSystem

@pytest.fixture
def trading_system():
    trading_system = AutoTradingSystem()
    trading_system.select_stock_broker("Kiwer")
    trading_system.login("test", "1234")

def test_basic_function_select_broker():
    trading_system = AutoTradingSystem()

    trading_system.select_stock_broker("Kiwer")
    assert trading_system.get_stock_broker() == "Kiwer"

    trading_system.select_stock_broker("Nemo")
    assert trading_system.get_stock_broker() == "Nemo"


def test_basic_function_login_kiwer(capsys):
    trading_system = AutoTradingSystem()

    trading_system.select_stock_broker("Kiwer")
    trading_system.login("test", "1234")

    captured = capsys.readouterr()
    assert "test login success" in captured.out

def test_basic_function_login_nemo(capsys):
    trading_system = AutoTradingSystem()

    trading_system.select_stock_broker("Nemo")
    trading_system.login("test", "1234")

    captured = capsys.readouterr()
    assert "test login success" in captured.out

def test_basic_function_buy(capsys, trading_system):
    trading_system = AutoTradingSystem()

    trading_system.buy("1234", 10000, 10)
    captured = capsys.readouterr()
    assert "1234 : Buy stock ( 10000 * 10 )" in captured.out

def test_basic_function_sell(capsys, trading_system):
    trading_system = AutoTradingSystem()

    trading_system.sell("1234", 10000, 10)
    captured = capsys.readouterr()
    assert "1234 : Sell stock ( 10000 * 10 )" in captured.out

def test_basic_function_current_price(capsys, trading_system):
    trading_system = AutoTradingSystem()

    price = trading_system.current_price("1234")
    assert (price >=0 and price < 10000)