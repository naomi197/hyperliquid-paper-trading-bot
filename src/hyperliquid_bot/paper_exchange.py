from dataclasses import dataclass

@dataclass
class PaperAccount:
    cash: float
    position_size: float = 0.0
    entry_price: float = 0.0
    realized_pnl: float = 0.0

class PaperExchange:
    def __init__(self, initial_cash: float = 10000.0, fee_rate: float = 0.0005):
        self.account = PaperAccount(cash=initial_cash)
        self.fee_rate = fee_rate

    def execute_market_buy(self, size: float, price: float):
        cost = size * price
        fee = cost * self.fee_rate
        if self.account.cash >= (cost + fee):
            self.account.cash -= (cost + fee)
            self.account.position_size += size
            self.account.entry_price = price

    def execute_market_sell(self, size: float, price: float):
        sell_size = min(size, self.account.position_size)
        if sell_size <= 0:
            return
        revenue = sell_size * price
        fee = revenue * self.fee_rate
        pnl = (price - self.account.entry_price) * sell_size
        self.account.realized_pnl += pnl
        self.account.cash += (revenue - fee)
        self.account.position_size -= sell_size
