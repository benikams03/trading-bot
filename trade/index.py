import MetaTrader5 as mt5
from datetime import datetime

class Traide_default:
    def buy(symbol, lot):
        tick = mt5.symbol_info_tick(symbol)

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY,
            "price": tick.ask,
            "deviation": 10,
            "magic": 1001,
            "comment": "BUY",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        
        heure = datetime.now().strftime("%H:%M:%S")
        response = mt5.order_send(request)
        print(f"[{heure}] BUY: {symbol} {lot}")
        return response
    
    def sell(symbol, lot):
        tick = mt5.symbol_info_tick(symbol)

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_SELL,
            "price": tick.bid,
            "deviation": 10,
            "magic": 1001,
            "comment": "SELL",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        
        heure = datetime.now().strftime("%H:%M:%S")
        response = mt5.order_send(request)
        print(f"[{heure}] SELL: {symbol} {lot}")
        return response