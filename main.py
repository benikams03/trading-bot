from core.index import Core
from trade.index import Traide_default
import time
from analyse.safe import Safe
import MetaTrader5 as mt5

try:
    core = Core()
    if not core.connect():
        print("Impossible de se connecter à MT5. Arrêt du bot.")
        exit(1)

    while True:
        
        Traide_default.buy()

        time.sleep(5)

except Exception as e:
    print("Erreur:", e)
finally:
    core.shutdown()