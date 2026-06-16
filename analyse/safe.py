import MetaTrader5 as mt5
import pandas as pd
import dotenv
dotenv.load_dotenv()
import os

class Safe:
    def __init__(self, timeframe):
        self.symbol = os.getenv("SYMBOL")
        self.timeframe = timeframe
        self.candles = 250

    def get_data(self):
        data = mt5.copy_rates_from_pos(
            self.symbol,
            self.timeframe,
            0,
            self.candles
        )

        df = pd.DataFrame(data)

        return df

    def calculate_ema(self, df):

        df["ema50"] = df["close"].ewm(span=50).mean()
        df["ema200"] = df["close"].ewm(span=200).mean()

        return df

    def get_trend(self):

        df = self.get_data()

        df = self.calculate_ema(df)

        last_candle = df.iloc[-1]

        ema50 = last_candle["ema50"]
        ema200 = last_candle["ema200"]

        if ema50 > ema200:
            return "BUY"

        elif ema50 < ema200:
            return "SELL"

        return "NO TREND"
        