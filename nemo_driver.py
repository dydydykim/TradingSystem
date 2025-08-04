from stock_broker_driver_interface import StockBrokerDriverInterface
from nemo_api import NemoAPI


class NemoDriver(StockBrokerDriverInterface):
    def __init__(self):
        self._api = NemoAPI()

    def login(self, id: str, password: str) -> None:
        if id == "":
            raise ValueError("ID is empty!!")
        if password == "":
            raise ValueError("Password is empty!!")

        self._api.cerification(id=id, password=password)

    def buy(self, code: str, price: int, qty: int) -> None:
        if price < 0:
            raise ValueError("Price is under 0!!")
        if qty < 0:
            raise ValueError("Quantity is under 0!!")
        self._api.purchasing_stock(stock_code=code, price=price, count=qty)

    def sell(self, code: str, price: int, qty: int) -> None:
        if price < 0:
            raise ValueError("Price is under 0!!")
        if qty < 0:
            raise ValueError("Quantity is under 0!!")
        self._api.selling_stock(stock_code=code, price=price, count=qty)

    def get_price(self, code: str) -> int:
        return self._api.get_market_price(stock_code=code, minute=0)
