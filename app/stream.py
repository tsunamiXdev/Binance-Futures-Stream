from __future__ import annotations
from websocket import connect
import asyncio
import json

from .io_csv import Csvlink
from .formatter import PrettyPrinter

#create different symbol stream
class SymbolStreamer:
  def __init__ (self, we_base: str, symbol: str, sink: CsvSink, printer: PrettyPrinter):
    self.uri = f"{we_base}
