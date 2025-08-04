from stock_broker_driver_interface import StockBrokerDriverInterface
from kiwer_api import KiwerAPI


class KiwerDriver(StockBrokerDriverInterface):
    def __init__(self):
        self._api = KiwerAPI()

    def login(self, id: str, password: str) -> None:
        if id == "":
            raise ValueError("ID is empty!!")
        if password == "":
            raise ValueError("Password is empty!!")

        self._api.login(id=id, password=password)

    def buy(self, code: str, price: int, qty: int) -> None:
        if price < 0:
            raise ValueError("Price is under 0!!")
        if qty < 0:
            raise ValueError("Quantity is under 0!!")
        self._api.buy(stock_code=code, count=qty, price=price)

    def sell(self, code: str, price: int, qty: int) -> None:
        if price < 0:
            raise ValueError("Price is under 0!!")
        if qty < 0:
            raise ValueError("Quantity is under 0!!")
        self._api.sell(stock_code=code, count=qty, price=price)

    def get_price(self, code: str) -> int:
        return self._api.current_price(stock_code=code)
