import time

class AutoTradingSystem:
    def __init__(self):
        self._broker_name = ""
        self._balance = 0

    def select_stock_broker(self, name):
        self._broker_name = name

    def login(self, name, password):
        print("test login success")

    def get_stock_broker(self):
        return self._broker_name

    def buy(self, code: str, price, quantity):
        print(f'{code} : Buy stock ( {price} * {quantity} )')

    def sell(self, code: str, price, quantity):
        print(f'{code} : Sell stock ( {price} * {quantity} )')

    def get_price(self, code: str):
        return 100

    def set_balance(self, balance):
        self._balance = balance

    def buy_nice_timing(self, item):
        prior_stock_price = 0
        for _ in range(3):
            current_stock_price = self.get_price(item)
            if prior_stock_price >= current_stock_price:
                return
            prior_stock_price = current_stock_price
            time.sleep(0.2)

        number_of_stocks = self._balance // current_stock_price
        self.buy(item, current_stock_price, number_of_stocks)
        self._balance -= (current_stock_price * number_of_stocks)

    def sell_nice_timing(self, item, number_of_stocks):
        prior_stock_price = float('inf')
        for _ in range(3):
            current_stock_price = self.get_price(item)
            if prior_stock_price <= current_stock_price(item):
                return
            prior_stock_price = current_stock_price
            time.sleep(0.2)

        self.sell(item, current_stock_price, number_of_stocks)
        self._balance += (current_stock_price * number_of_stocks)