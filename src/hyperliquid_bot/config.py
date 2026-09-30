# Hyperliquid Paper Trading Bot

A modular, asynchronous Python trading bot designed for the Hyperliquid L1 ecosystem. It features market data ingestion, an EMA crossover strategy, deterministic risk management, and an offline paper execution engine.

> **Disclaimer:** This software is intended purely for educational and research purposes. No real orders are executed on-chain.

## Features
- **Public Market Data Client:** Async metadata and candle ingestion via public Hyperliquid info endpoints.
- **Pure Strategy Engine:** Moving average crossover logic with configurable parameters.
- **Risk & Sizing Module:** Enforces risk-per-trade limits and maximum notional exposure.
- **Paper Exchange:** Deterministic simulated order execution, tracking realized/unrealized PnL and fee accounting.

## Architecture
\\\	ext
hyperliquid-paper-trading-bot/
├── src/hyperliquid_bot/
│   ├── config.py
│   ├── models.py
│   ├── strategy.py
│   ├── risk.py
│   ├── paper_exchange.py
│   ├── market.py
│   ├── runner.py
│   └── cli.py
├── tests/
├── requirements.txt
└── README.md
\\\

## Quick Start
\\\ash
pip install -r requirements.txt
python -m hyperliquid_bot.cli --demo
\\\
"@ | Set-Content -Path "README.md" -Encoding utf8

# __init__.py
"" | Set-Content -Path "src\hyperliquid_bot\__init__.py" -Encoding utf8
"" | Set-Content -Path "tests\__init__.py" -Encoding utf8

# config.py
@"
from dataclasses import dataclass
import os

@dataclass
class BotConfig:
    symbol: str = "BTC"
    interval: str = "1h"
    initial_cash: float = 10000.0
    risk_per_trade: float = 0.01
    max_notional: float = 1000.0
    fast_ema: int = 9
    slow_ema: int = 21

    @classmethod
    def from_env(cls) -> "BotConfig":
        return cls(
            symbol=os.getenv("DEFAULT_SYMBOL", "BTC"),
            interval=os.getenv("CANDLE_INTERVAL", "1h"),
            initial_cash=float(os.getenv("INITIAL_CASH", "10000.0")),
            risk_per_trade=float(os.getenv("RISK_PER_TRADE", "0.01")),
            max_notional=float(os.getenv("MAX_NOTIONAL", "1000.0")),
        )
