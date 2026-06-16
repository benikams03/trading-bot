import MetaTrader5 as mt5
import dotenv
dotenv.load_dotenv()
import os


class Core:
    def __init__(self):
        self.username = os.getenv("MT5_USERNAME")
        self.password = os.getenv("MT5_PASSWORD")
        self.server = os.getenv("MT5_SERVER")
        
    def connect(self):
        if not mt5.initialize():
            print("Erreur init MT5:", mt5.last_error())
            return False

        if mt5.login(int(self.username), password=self.password, server=self.server):
            print("--------------------------------")
            print("     MT5 TRADING BOT v1.0")
            print("--------------------------------", "")
            print("[SUCCESS] Connecté MT5")
            print("Nom     : ", self.get_account_info().name, "")
            print("Solde   : ", self.get_account_info().balance, self.get_account_info().currency)
            print("Symbol  : ", os.getenv("SYMBOL"))
            print("Lot Size: ", os.getenv("LOT_SIZE"))
            print("--------------------------------", "")
            return mt5
        else:
            print("Erreur login", mt5.last_error())
            return False

    def get_account_info(self):
        return mt5.account_info()
        
    def shutdown(self):
        mt5.shutdown()