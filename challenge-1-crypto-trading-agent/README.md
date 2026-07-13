# Challenge 1 — AI Agent Creation Platform for Autonomous Crypto Trading

## Problem Statement

Develop an intelligent platform that enables users to create, configure, deploy, and evaluate autonomous AI-powered crypto trading agents with minimal coding. The platform should support customizable agent workflows, trading strategies, and explainable decision-making while allowing users to simulate, monitor, and continuously improve agent performance.

---

## Resources Overview

| # | Resource | Type | Login Required |
|---|----------|------|----------------|
| 1 | Binance Vision | Historical Market Data | ❌ None |
| 2 | CCXT | Exchange Integration Library | ❌ None |
| 3 | pandas-ta Classic | Technical Indicators Library | ❌ None |
| 4 | Backtesting.py | Backtesting / Paper Trading | ❌ None |
| 5 | Fear & Greed Index | Market Sentiment | ❌ None |
| 6 | Freqtrade Strategies | Sample Trading Strategies | ❌ None |
| 7 | Freqtrade Strategy Template | Strategy Customization Guide | ❌ None |

---

## 1. Historical Market Data — Binance Vision

**Source:** https://data.binance.vision

Official Binance historical market data portal. Provides BTC, ETH, SOL, XRP OHLCV candlestick data, raw trades, and klines across multiple timeframes (1m, 5m, 1h, 1d, etc.).

**What you get:**
- `BTCUSDT-1h-*.zip` — Hourly OHLCV klines
- `ETHUSDT-1d-*.zip` — Daily OHLCV klines
- `*-trades-*.zip` — Raw tick-level trade data
- Coverage: 2017–present

**Download (no login):**
```bash
# Example: BTC/USDT daily klines for 2024
wget "https://data.binance.vision/data/spot/monthly/klines/BTCUSDT/1d/BTCUSDT-1d-2024-01.zip"
unzip BTCUSDT-1d-2024-01.zip -d data/ohlcv/

# Python download script
python -c "
import urllib.request, zipfile, os
pairs = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'XRPUSDT']
os.makedirs('data/ohlcv', exist_ok=True)
for pair in pairs:
    url = f'https://data.binance.vision/data/spot/monthly/klines/{pair}/1d/{pair}-1d-2024-01.zip'
    dest = f'data/ohlcv/{pair}-1d-2024-01.zip'
    print(f'Downloading {pair}...')
    urllib.request.urlretrieve(url, dest)
    with zipfile.ZipFile(dest) as z: z.extractall('data/ohlcv/')
    os.remove(dest)
print('Done')
"
```

**Column format:** `open_time, open, high, low, close, volume, close_time, quote_volume, count, taker_buy_volume, taker_buy_quote_volume, ignore`

---

## 2. Exchange Integration — CCXT

**GitHub:** https://github.com/ccxt/ccxt
**Docs:** https://docs.ccxt.com

Unified Python/JS API for 100+ cryptocurrency exchanges (Binance, Coinbase, Kraken, OKX, Bybit, etc.). Use this to fetch live prices, place paper-trade orders, and integrate real-time data into your agent.

**Install:**
```bash
pip install ccxt
```

**Quick Start:**
```python
import ccxt

# Fetch live OHLCV from Binance (no API key needed for public data)
exchange = ccxt.binance()
ohlcv = exchange.fetch_ohlcv('BTC/USDT', timeframe='1h', limit=100)

import pandas as pd
df = pd.DataFrame(ohlcv, columns=['timestamp','open','high','low','close','volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
print(df.tail())
```

**For paper trading (simulated orders):**
```python
# Use Binance testnet — no real money
exchange = ccxt.binance({
    'apiKey': 'YOUR_TESTNET_KEY',
    'secret': 'YOUR_TESTNET_SECRET',
    'options': {'defaultType': 'spot'},
    'urls': {'api': {'public': 'https://testnet.binance.vision/api'}}
})
order = exchange.create_order('BTC/USDT', 'market', 'buy', 0.001)
```

---

## 3. Technical Indicators — pandas-ta Classic

**GitHub:** https://github.com/xgboosted/pandas-ta-classic

Drop-in pandas extension providing 150+ technical indicators: RSI, MACD, EMA, SMA, Bollinger Bands, ATR, ADX, VWAP, OBV, and more.

**Install:**
```bash
pip install pandas-ta-classic
```

**Quick Start:**
```python
import pandas as pd
import pandas_ta as ta

# Load your OHLCV data
df = pd.read_csv('data/ohlcv/BTCUSDT-1d-2024-01.csv',
    names=['open_time','open','high','low','close','volume',
           'close_time','quote_vol','count','taker_buy_vol','taker_buy_quote','ignore'])

# Add indicators in one line
df.ta.rsi(length=14, append=True)          # RSI-14
df.ta.macd(fast=12, slow=26, append=True)  # MACD
df.ta.bbands(length=20, append=True)       # Bollinger Bands
df.ta.ema(length=50, append=True)          # EMA-50
df.ta.atr(length=14, append=True)          # ATR-14
df.ta.vwap(append=True)                    # VWAP
df.ta.obv(append=True)                     # OBV

print(df[['close','RSI_14','MACD_12_26_9','BBM_20_2.0']].tail(10))
```

---

## 4. Backtesting / Paper Trading — Backtesting.py

**GitHub:** https://github.com/kernc/backtesting.py

Lightweight, fast Python framework for backtesting trading strategies. Use this to simulate your agent's trading decisions on historical data before live deployment.

**Install:**
```bash
pip install backtesting
```

**Quick Start:**
```python
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd
import pandas_ta as ta

# Load data
df = pd.read_csv('data/ohlcv/BTCUSDT-1d-2024-01.csv',
    names=['Open','High','Low','Close','Volume'],
    usecols=[1,2,3,4,5])
df.index = pd.date_range('2024-01-01', periods=len(df), freq='D')

# Define a simple RSI strategy
class RsiStrategy(Strategy):
    rsi_upper = 70
    rsi_lower = 30

    def init(self):
        close = pd.Series(self.data.Close)
        self.rsi = self.I(lambda: ta.rsi(close, length=14))

    def next(self):
        if self.rsi[-1] < self.rsi_lower:
            self.buy()
        elif self.rsi[-1] > self.rsi_upper:
            self.sell()

# Run backtest
bt = Backtest(df, RsiStrategy, cash=10000, commission=0.001)
stats = bt.run()
print(stats[['Return [%]', 'Win Rate [%]', 'Sharpe Ratio', 'Max. Drawdown [%]']])
bt.plot()
```

---

## 5. Market Sentiment — Fear & Greed Index

**Source:** https://alternative.me/crypto/fear-and-greed-index/

Daily crypto market sentiment index (0 = Extreme Fear, 100 = Extreme Greed). Use as a trading signal or feature input to your agent.

**Download (no login, free API):**
```python
import requests
import pandas as pd

# Fetch last 365 days of Fear & Greed data
url = "https://api.alternative.me/fng/?limit=365&format=json"
response = requests.get(url).json()

df = pd.DataFrame(response['data'])
df['value'] = pd.to_numeric(df['value'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
df = df.sort_values('timestamp').reset_index(drop=True)
df.to_csv('data/sentiment/fear_greed_index.csv', index=False)

print(df.tail())
# timestamp    value    value_classification
# 2024-01-15   72       Greed
# 2024-01-16   68       Greed
```

---

## 6. Sample Trading Strategies — Freqtrade

**GitHub:** https://github.com/freqtrade/freqtrade-strategies

Production-tested trading strategies built for the Freqtrade framework. Study these to understand how real-world trading agents are structured: entry/exit conditions, risk management, indicator usage.

**Key strategies to study:**
- `SampleStrategy.py` — canonical reference implementation
- `NostalgiaForInfinityX.py` — complex multi-indicator strategy
- `BbandRsi.py` — Bollinger Band + RSI combination

```bash
# Clone the strategies repo
git clone https://github.com/freqtrade/freqtrade-strategies.git data/strategies/
```

---

## 7. Strategy Template & Customization Guide — Freqtrade

**Template:** https://github.com/freqtrade/freqtrade/blob/develop/freqtrade/templates/sample_strategy.py
**Guide:** https://www.freqtrade.io/en/stable/strategy-customization/

The official Freqtrade strategy template shows exactly how an autonomous trading agent is structured: indicator computation, buy/sell signal generation, stop-loss, ROI, and trailing stop configuration.

**Study the structure:**
```python
class MyTradingAgent(IStrategy):
    # Minimal ROI — exit when profit target hit
    minimal_roi = {"60": 0.01, "30": 0.02, "0": 0.04}

    # Stop-loss configuration
    stoploss = -0.10

    # Trailing stop
    trailing_stop = True
    trailing_stop_positive = 0.01

    def populate_indicators(self, dataframe, metadata):
        # Add RSI, MACD, etc. here
        dataframe['rsi'] = ta.RSI(dataframe['close'], timeperiod=14)
        return dataframe

    def populate_entry_trend(self, dataframe, metadata):
        dataframe.loc[dataframe['rsi'] < 30, 'enter_long'] = 1
        return dataframe

    def populate_exit_trend(self, dataframe, metadata):
        dataframe.loc[dataframe['rsi'] > 70, 'exit_long'] = 1
        return dataframe
```

---

## Folder Structure

```
challenge-1-crypto-trading-agent/
├── README.md                    ← This file
├── download.py                  ← Auto-download script
└── data/
    ├── ohlcv/                   ← Binance Vision klines (BTC, ETH, SOL, XRP)
    ├── sentiment/               ← Fear & Greed Index CSV
    ├── indicators/              ← Pre-computed indicator outputs
    └── strategies/              ← Freqtrade strategy examples
```

---

## Recommended Setup

```bash
# Install all dependencies
pip install ccxt backtesting pandas-ta-classic requests pandas numpy

# Run the download script
python download.py
```

---

## Suggested Build Path for Participants

1. **Download data** → `python download.py` (Binance Vision + Fear & Greed)
2. **Compute indicators** → pandas-ta-classic on OHLCV data
3. **Study strategy templates** → Freqtrade strategies repo
4. **Build your agent** → define entry/exit logic using indicators + sentiment
5. **Backtest** → Backtesting.py to evaluate performance (Return, Sharpe, Drawdown)
6. **Exchange integration** → CCXT for paper trading / live simulation

---

*Tech Mahindra CODE Hackathon — Challenge 1 Dataset*
