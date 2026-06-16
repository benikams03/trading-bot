from core.index import Core
from trade.strategy import StrategyTrade
import time
from analyse.safe import Safe
import MetaTrader5 as mt5
from datetime import datetime

try:
    core = Core()
    if not core.connect():
        print("Impossible de se connecter à MT5. Arrêt du bot.")
        exit(1)

    while True:
        
        StrategyTrade().start("BUY", 5)

        heure = datetime.now().strftime("%H:%M:%S")
        print(f'[{heure}] ANALYZING MARKET.')
        time.sleep(1)
        print(f'[{heure}] ANALYZING MARKET...')
        time.sleep(1)
        print(f'[{heure}] ANALYZING MARKET....')
        time.sleep(1)
        print(f'[{heure}] ANALYZING MARKET.....')
        time.sleep(1)
        print(f'[{heure}] ANALYZING MARKET......')
        time.sleep(1)

        Safe(mt5.TIMEFRAME_M1).get_trend()

        print('')


        # Check if there are any open positions
        # positions = mt5.positions_get()
        # if positions is None or len(positions) == 0:
        #     print("Aucune position ouverte")
        # else:
        #     print(f"Il y a {len(positions)} position(s) ouverte(s)")
        #     # Close all positions
        #     Traide_default.close_all()


except Exception as e:
    print("Erreur:", e)
finally:
    core.shutdown()