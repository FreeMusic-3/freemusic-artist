import io
from abc import abstractmethod
from typing import Protocol, Sequence, Any

from fastapi import FastAPI
from opentelemetry.metrics import Meter
from opentelemetry.trace import Tracer
from weed.util import WeedOperationResponse




class IStorage(Protocol):
    @abstractmethod
    def delete(self, fid: str, name: str): pass

    @abstractmethod
    def download(self, fid: str, name: str) -> tuple[io.BytesIO, str]: pass

    @abstractmethod
    def upload(self, file: io.BytesIO, name: str) -> WeedOperationResponse: pass

    @abstractmethod
    def update(self, file: io.BytesIO, fid: str, name: str): pass


class IDB(Protocol):

    @abstractmethod
    async def insert(self, query: str, query_params: dict) -> int: pass

    @abstractmethod
    async def delete(self, query: str, query_params: dict) -> None: pass

    @abstractmethod
    async def update(self, query: str, query_params: dict) -> None: pass

    @abstractmethod
    async def select(self, query: str, query_params: dict) -> Sequence[Any]: pass

    @abstractmethod
    async def multi_query(self, queries: list[str]) -> None: pass