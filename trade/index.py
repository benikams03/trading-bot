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
        print(f"[{heure}] POSITION OPENED | BUY {os.getenv('SYMBOL')} | Entry: {response.price} | Volume: {response.volume} | Deal: {response.deal}")
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
        print(f"[{heure}] POSITION OPENED | SELL {os.getenv('SYMBOL')} | Entry: {response.price} | Volume: {response.volume} | Deal: {response.deal}")
        return response
    
    def close_all():
        positions = mt5.positions_get()
        if positions is None or len(positions) == 0:
            print("Aucune position ouverte à fermer")
            return
        
        for position in positions:
            tick = mt5.symbol_info_tick(position.symbol)
            
            # Déterminer le type d'ordre inverse
            order_type = mt5.ORDER_TYPE_SELL if position.type == mt5.POSITION_TYPE_BUY else mt5.ORDER_TYPE_BUY
            price = tick.bid if position.type == mt5.POSITION_TYPE_BUY else tick.ask
            
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": position.symbol,
                "volume": position.volume,
                "type": order_type,
                "position": position.ticket,  # Ticket de la position à fermer
                "price": price,
                "deviation": 10,
                "magic": 1001,
                "comment": "CLOSE",
                "type_time": mt5.ORDER_TIME_GTC,
            }
            
            heure = datetime.now().strftime("%H:%M:%S")
            response = mt5.order_send(request)
            
            profit = position.profit
            profit_color = "\033[92m" if profit >= 0 else "\033[91m"
            reset_color = "\033[0m"
            
            print(f"[{heure}] POSITION CLOSED | {position.symbol} | Ticket: {position.ticket} | Profit: {profit_color}{profit:.2f}{reset_color}")