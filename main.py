from core.index import Core
from trade.index import Traide_default
import time

try:
    core = Core()
    core.connect()
    account_info = core.get_account_info()

    while True:
        
        Traide_default.buy("EURUSD", 0.1)
        time.sleep(5)

except Exception as e:
    print("Erreur:", e)
finally:
    core.shutdown()