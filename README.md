# Hyperliquid Paper Trading Bot

A lightweight, risk-managed paper-trading simulator for testing Hyperliquid-style strategies without using real funds. It calculates position size from configurable limits, simulates market orders, and tracks cash, positions, and realized P&L.

## Features

- Deterministic paper-trading workflow with no live orders or exchange credentials
- Configurable symbol, starting balance, risk per trade, and maximum notional exposure
- Separate models for account state, risk management, and simulated execution
- Simple command-line demo for quickly validating the trading flow

## Quick Start

Requires Python 3.10 or newer.

```bash
git clone https://github.com/naomi197/hyperliquid-paper-trading-bot.git
cd hyperliquid-paper-trading-bot
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
cp .env.example .env
PYTHONPATH=src python -m hyperliquid_bot.cli
```

On Windows PowerShell, run the final command as:

```powershell
$env:PYTHONPATH = "src"
python -m hyperliquid_bot.cli
```

## Safety

This project is for simulation and portfolio demonstration only. It does not connect to a live exchange, place real orders, or manage real funds.
