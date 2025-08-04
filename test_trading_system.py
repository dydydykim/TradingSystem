import pytest
from pytest_mock import MockerFixture
from auto_trading_system import AutoTradingSystem
from kiwer_driver import KiwerDriver
from nemo_driver import NemoDriver


def mocker_login(id):
    print(id + ' login success')


def mocker_buy():
    print("1234 : Buy stock ( 10000 * 10 )")


def mocker_sell():
    print("1234 : Sell stock ( 10000 * 10 )")


@pytest.fixture
def trading_system():
    trading_system = AutoTradingSystem()
    trading_system.select_stock_broker("Kiwer")
    trading_system.login("test", "1234")
    return trading_system


def test_basic_function_select_broker(trading_system):
    trading_system.select_stock_broker("Kiwer")
    assert trading_system.get_stock_broker() == "Kiwer"

    trading_system.select_stock_broker("Nemo")
    assert trading_system.get_stock_broker() == "Nemo"


def test_basic_function_login_kiwer(capsys, trading_system, mocker: MockerFixture):
    driver: KiwerDriver = mocker.Mock()
    driver.login.side_effect = mocker_login
    trading_system.select_stock_broker("Kiwer")
    trading_system.login("test", "1234")
    captured = capsys.readouterr()
    assert "test login success" in captured.out


def test_basic_function_login_nemo(capsys, trading_system, mocker: MockerFixture):
    driver: NemoDriver = mocker.Mock()
    driver.login.side_effect = mocker_login
    trading_system.select_stock_broker("Nemo")
    trading_system.login("test", "1234")
    captured = capsys.readouterr()
    assert "test login success" in captured.out


def test_basic_function_buy(capsys, trading_system, mocker: MockerFixture):
    driver: KiwerDriver = mocker.Mock()
    driver.buy.side_effect = mocker_buy
    trading_system.buy("1234", 10000, 10)
    captured = capsys.readouterr()
    assert "1234 : Buy stock ( 10000 * 10 )" in captured.out


def test_basic_function_sell(capsys, trading_system, mocker: MockerFixture):
    driver: KiwerDriver = mocker.Mock()
    driver.sell.side_effect = mocker_sell
    trading_system.sell("1234", 10000, 10)
    captured = capsys.readouterr()
    assert "1234 : Sell stock ( 10000 * 10 )" in captured.out


def test_basic_function_current_price(capsys, trading_system, mocker: MockerFixture):
    driver: KiwerDriver = mocker.Mock()
    driver.current_price.return_value = 100
    price = trading_system.current_price("1234")
    assert price == 100
