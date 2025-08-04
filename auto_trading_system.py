class AutoTradingSystem:
    def __init__(self):
        self._broker_name = ""

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

    def current_price(self, code: str):
        return 100