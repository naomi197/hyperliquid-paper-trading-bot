import argparse
from hyperliquid_bot.config import BotConfig
from hyperliquid_bot.paper_exchange import PaperExchange
from hyperliquid_bot.risk import RiskManager

def main():
    parser = argparse.ArgumentParser(description="Hyperliquid Paper Trading Bot CLI")
    parser.add_argument("--demo", action="store_true", help="Run deterministic simulation demo")
    args = parser.parse_args()

    config = BotConfig.from_env()
    risk = RiskManager(config.risk_per_trade, config.max_notional)
    exchange = PaperExchange(config.initial_cash)

    print(f"[*] Hyperliquid Paper Bot Initialized for {config.symbol}")
    print(f"[*] Starting Cash: ")
    
    price = 65000.0
    size = risk.calculate_size(exchange.account.cash, price)
    print(f"[*] Risk Sizing: calculated position size = {size} {config.symbol} at ")
    
    exchange.execute_market_buy(size, price)
    print(f"[*] Executed Paper BUY -> Position: {exchange.account.position_size} {config.symbol}")
    
    exit_price = 67000.0
    exchange.execute_market_sell(size, exit_price)
    print(f"[*] Executed Paper SELL at  -> Realized PnL: ")

if __name__ == "__main__":
    main()
