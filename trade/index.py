import MetaTrader5 as mt5
from datetime import datetime
import dotenv
dotenv.load_dotenv()
import os

class Traide_default:
    def buy():
        tick = mt5.symbol_info_tick(os.getenv("SYMBOL"))

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": os.getenv("SYMBOL"),
            "volume": float(os.getenv("LOT_SIZE")),
            "type": mt5.ORDER_TYPE_BUY,
            "price": tick.ask,
            "deviation": 10,
            "magic": 1001,
            "comment": "BUY",
            "type_time": mt5.ORDER_TIME_GTC,
        }
        
        heure = datetime.now().strftime("%H:%M:%S")
        response = mt5.order_send(request)
        print(f"[{heure}] BUY: {os.getenv('SYMBOL')} {os.getenv('LOT_SIZE')}")
        return response
    
    def sell():
        tick = mt5.symbol_info_tick(os.getenv("SYMBOL"))

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": os.getenv("SYMBOL"),
            "volume": float(os.getenv("LOT_SIZE")),
            "type": mt5.ORDER_TYPE_SELL,
            "price": tick.bid,
            "deviation": 10,
            "magic": 1001,
            "comment": "SELL",
            "type_time": mt5.ORDER_TIME_GTC,
        }
        
        heure = datetime.now().strftime("%H:%M:%S")
        response = mt5.order_send(request)
        print(f"[{heure}] SELL: {os.getenv('SYMBOL')} {os.getenv('LOT_SIZE')}")
        return response