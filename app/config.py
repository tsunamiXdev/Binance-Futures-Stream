from __future__ import annotations
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
symbols: tuple[str, ...]
ws_base: str
csv_file: str
tz: str
thr_large: float
thr_med: float
thr_small: float

@staticmethod
def _parse_symbols(s: str | None) -> tuple[str, ...]:
if not s:
return ("btcusdt", "ethusdt")
return tuple(x.strip().lower() for x in s.split(",") if x.strip())

@classmethod
def load(cls) -> "Settings":
return cls(
symbols=cls._parse_symbols(os.getenv("SYMBOLS")),
ws_base=os.getenv("WS_BASE", "wss://fstream.binance.com/ws"),
csv_file=os.getenv("CSV_FILE", "binance_trades.csv"),
tz=os.getenv("TZ", "US/Eastern"),
thr_large=float(os.getenv("THRESHOLD_LARGE", 100_000)),
thr_med=float(os.getenv("THRESHOLD_MED", 50_000)),
thr_small=float(os.getenv("THRESHOLD_SMALL", 15_000)),
)

SETTINGS = Settings.load()
