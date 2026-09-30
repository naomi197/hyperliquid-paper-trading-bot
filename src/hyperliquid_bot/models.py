from dataclasses import dataclass
from typing import Optional

@dataclass
class Candle:
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: float

@dataclass
class Signal:
    action: str  # BUY, SELL, HOLD
    confidence: float
    reason: str

@dataclass
class Position:
    symbol: str
    size: float
    entry_price: float
