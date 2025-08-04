import pytest
import pytest_mock
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
    return trading_system


def test_basic_function_select_broker(trading_system, mocker: MockerFixture):
    driver: KiwerDriver = mocker.Mock()
    trading_system.select_stock_broker("Kiwer", driver)
    assert trading_system.get_stock_broker() == "Kiwer"

    driver: NemoDriver = mocker.Mock()
    trading_system.select_stock_broker("Nemo", driver)
    assert trading_system.get_stock_broker() == "Nemo"


def test_basic_function_login_kiwer(capsys, trading_system, mocker: MockerFixture):
    driver: KiwerDriver = mocker.Mock()
    driver.login.side_effect = mocker_login
    trading_system.select_stock_broker("Kiwer", driver)
    trading_system.login("test", "1234")

    captured = capsys.readouterr()
    assert "test login success" in captured.out
    driver.login.assert_called()

def test_basic_function_login_nemo(capsys, trading_system, mocker: MockerFixture):
    driver: NemoDriver = mocker.Mock()
    driver.login.side_effect = mocker_login
    trading_system.select_stock_broker("Nemo", driver)
    trading_system.login("test", "1234")

    captured = capsys.readouterr()
    assert "test login success" in captured.out
    driver.login.assert_called()

def test_basic_function_buy(capsys, trading_system, mocker: MockerFixture):
    driver: KiwerDriver = mocker.Mock()
    driver.buy.side_effect = mocker_buy

    trading_system.select_stock_broker("Kiwer", driver)
    trading_system.buy("1234", 10000, 10)

    captured = capsys.readouterr()
    assert "1234 : Buy stock ( 10000 * 10 )" in captured.out
    driver.buy.assert_called()

def test_basic_function_sell(capsys, trading_system, mocker: MockerFixture):
    driver: KiwerDriver = mocker.Mock()
    driver.sell.side_effect = mocker_sell

    trading_system.select_stock_broker("Kiwer", driver)

    trading_system.sell("1234", 10000, 10)

    captured = capsys.readouterr()
    assert "1234 : Sell stock ( 10000 * 10 )" in captured.out
    driver.sell.assert_called()


def test_basic_function_current_price(capsys, trading_system, mocker: MockerFixture):
    driver: KiwerDriver = mocker.Mock()
    driver.get_price.return_value = 100
    trading_system.select_stock_broker("Kiwer", driver)

    price = trading_system.get_price("1234")
    assert price == 100
    driver.get_price.assert_called()


def test_buy_called_on_three_price_increase(mocker):
    buy_mock = mocker.patch('auto_trading_system.AutoTradingSystem.buy')
    ats = AutoTradingSystem()

    ats.set_balance(100000)
    ats.get_price = mocker.Mock(side_effect=[5000, 5100, 5200])
    ats.buy_nice_timing("1234")

    buy_mock.assert_called_once()


def test_buy_not_called_if_price_not_increasing(mocker):
    buy_mock = mocker.patch('auto_trading_system.AutoTradingSystem.buy')
    ats = AutoTradingSystem()

    ats.set_balance(100000)
    ats.get_price = mocker.Mock(side_effect=[5000, 4900, 4950])  # 상승 아님
    ats.buy_nice_timing("1234")

    buy_mock.assert_not_called()


def test_buy_called_on_three_price_decrease(mocker):
    sell_mock = mocker.patch('auto_trading_system.AutoTradingSystem.sell')
    ats = AutoTradingSystem()

    ats.set_balance(100000)
    ats.get_price = mocker.Mock(side_effect=[5500, 5400, 5300])
    number_of_stock = 10
    ats.sell_nice_timing("1234", number_of_stock)

    sell_mock.assert_called_once()


def test_buy_not_called_if_price_not_decreasing(mocker):
    sell_mock = mocker.patch('auto_trading_system.AutoTradingSystem.sell')
    ats = AutoTradingSystem()

    ats.set_balance(100000)
    ats.get_price = mocker.Mock(side_effect=[5500, 5400, 5550])  # 상승 아님
    number_of_stock = 10
    ats.sell_nice_timing("1234", number_of_stock)

    sell_mock.assert_not_called()