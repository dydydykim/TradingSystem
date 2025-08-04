from abc import ABC, abstractmethod

class StockBrokerDriverInterface(ABC):
    @abstractmethod
    def login(self, id: str, password: str) -> None:
        pass

    @abstractmethod
    def buy(self, code: str, price: int, qty: int) -> None:
        pass

    @abstractmethod
    def sell(self, code: str, price: int, qty: int) -> None:
        pass

    @abstractmethod
    def get_price(self, code: str) -> int:
        pass