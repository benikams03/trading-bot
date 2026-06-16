import time
from datetime import datetime
from trade.index import Traide_default

class StrategyTrade:
    def start(self, order_type, size = 1, time_sleep = 5):

        heure = datetime.now().strftime("%H:%M:%S")
        if order_type == "BUY":
            for _ in range(size):
                Traide_default.buy()

            print(f'[{heure}] Next check in {time_sleep}s... ')
            time.sleep(time_sleep)

            Traide_default.close_all()
            print('')

        elif order_type == "SELL":
            for _ in range(size):
                Traide_default.sell()
            print(f'[{heure}] Next check in {time_sleep}s... ')
            time.sleep(time_sleep)

            Traide_default.close_all()
            print('')