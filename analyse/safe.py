import MetaTrader5 as mt5
import pandas as pd
import dotenv
dotenv.load_dotenv()
import os

class Safe:
    
    #Initialise la classe Safe avec le timeframe spécifié.
    def __init__(self, timeframe):
        self.symbol = os.getenv("SYMBOL")
        self.timeframe = timeframe
        self.candles = 250


    #Récupère les données de prix depuis MetaTrader5.
    #Contient les données OHLCV (Open, High, Low, Close, Volume)
    #pour le nombre de bougies spécifié (250 par défaut)
    def get_data(self):
        data = mt5.copy_rates_from_pos(
            self.symbol,
            self.timeframe,
            0,
            self.candles
        )

        df = pd.DataFrame(data)

        return df

    
    #Calcule les moyennes mobiles exponentielles (EMA) 50 et 200.
    #Le DataFrame original avec deux nouvelles colonnes:
    #  - ema50: EMA sur 50 périodes
    #  - ema200: EMA sur 200 périodes
    def calculate_ema(self, df):
        df["ema50"] = df["close"].ewm(span=50).mean()
        df["ema200"] = df["close"].ewm(span=200).mean()

        return df


    #Détermine la tendance du marché en comparant les EMA 50 et 200.
    
    #Stratégie:
    # - Si EMA 50 > EMA 200: Tendance haussière (BUY)
    # - Si EMA 50 < EMA 200: Tendance baissière (SELL)
    # - Si EMA 50 = EMA 200: Pas de tendance détectée
    def get_trend(self):
        df = self.get_data()

        df = self.calculate_ema(df)

        last_candle = df.iloc[-1]

        ema50 = last_candle["ema50"]
        ema200 = last_candle["ema200"]

        profit_color = "\033[92m" if ema50 > ema200 else "\033[91m"
        reset_color = "\033[0m"

        if ema50 > ema200:
            print(f"{profit_color}Tendance haussière (BUY){reset_color}")
            return "BUY"

        elif ema50 < ema200:
            print(f"{profit_color}Tendance baissière (SELL){reset_color}")
            return "SELL"

        return "NO TREND"
        