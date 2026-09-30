class RiskManager:
    def __init__(self, risk_per_trade: float, max_notional: float):
        self.risk_per_trade = risk_per_trade
        self.max_notional = max_notional

    def calculate_size(self, balance: float, current_price: float, stop_loss_pct: float = 0.02) -> float:
        if current_price <= 0 or balance <= 0:
            return 0.0
        risk_amount = balance * self.risk_per_trade
        per_unit_risk = current_price * stop_loss_pct
        size = risk_amount / per_unit_risk
        notional = size * current_price
        if notional > self.max_notional:
            size = self.max_notional / current_price
        return round(size, 4)
