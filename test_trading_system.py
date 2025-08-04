import pytest
import pytest_mock
from pytest_mock import MockerFixture

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


def test_buy_called_on_three_price_increase(mocker):
    buy_mock = mocker.patch('auto_trading_system.AutoTradingSystem.buy')
    ats = AutoTradingSystem()

    ats.set_balance(100000)
    ats.get_price = mocker.Mock(side_effect=[5000, 5100, 5200])
    ats.buyNiceTiming()

    buy_mock.assert_called_once()


def test_buy_not_called_if_price_not_increasing(mocker):
    buy_mock = mocker.patch('auto_trading_system.AutoTradingSystem.buy')
    ats = AutoTradingSystem()

    ats.set_balance(100000)
    ats.get_price = mocker.Mock(side_effect=[5000, 4900, 4950])  # 상승 아님
    ats.buyNiceTiming()

    buy_mock.assert_not_called()