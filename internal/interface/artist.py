from abc import abstractmethod
from typing import Protocol, List

from fastapi import UploadFile

from internal import model


class IArtistController(Protocol):
    @abstractmethod
    async def create_artist(
            self,
            account_id: int,
            avatar_file: UploadFile,
            name: str,
            description: str,
    ) -> int: pass

    @abstractmethod
    async def edit_name(self, artist_id: int, name: str) -> None: pass

    @abstractmethod
    async def edit_avatar(self, account_id: int, avatar_file: UploadFile ) -> None: pass

    @abstractmethod
    async def edit_description(self, artist_id: int, description: str) -> None: pass

    @abstractmethod
    async def increment_artist_like(self, artist_id: int) -> None: pass

    @abstractmethod
    async def decrement_artist_like(self, artist_id: int) -> None: pass

    @abstractmethod
    async def add_listener(self, artist_id: int, listener_id: int) -> None: pass

    @abstractmethod
    async def get_all_artist(self) -> List[model.Artist]: pass

    @abstractmethod
    async def get_listening_count_per_months(self, artist_id: int) -> int: pass


class IArtistService(Protocol):
    @abstractmethod
    async def create_artist(
            self,
            account_id: int,
            avatar_file: UploadFile,
            name: str,
            description: str
    ) -> int: pass

    @abstractmethod
    async def edit_name(self, artist_id: int, name: str) -> None: pass

    @abstractmethod
    async def edit_avatar(self, account_id: int, avatar_file: UploadFile) -> None: pass

    @abstractmethod
    async def edit_description(self, artist_id: int, description: str) -> None: pass

    @abstractmethod
    async def increment_artist_like(self, artist_id: int) -> None: pass

    @abstractmethod
    async def decrement_artist_like(self, artist_id: int) -> None: pass

    @abstractmethod
    async def add_listener(self, artist_id: int, listener_id: int) -> None: pass

    @abstractmethod
    async def get_all_artist(self) -> List[model.Artist]: pass

    @abstractmethod
    async def get_listening_count_per_months(self, artist_id: int) -> int: pass


class IArtistRepo(Protocol):
    @abstractmethod
    async def create_artist(
            self,
            account_id: int,
            avatar_fid: str,
            name: str,
            description: str
    ) -> int: pass

    @abstractmethod
    async def edit_name(self, artist_id: int, name: str) -> None: pass

    @abstractmethod
    async def edit_avatar(self, account_id: int, avatar_fid: str) -> None: pass

    @abstractmethod
    async def edit_description(self, artist_id: int, description: str) -> None: pass

    @abstractmethod
    async def increment_artist_like(self, artist_id: int) -> None: pass

    @abstractmethod
    async def decrement_artist_like(self, artist_id: int) -> None: pass

    @abstractmethod
    async def add_listener(self, artist_id: int, listener_id: int) -> None: pass

    @abstractmethod
    async def get_listener(self, artist_id: int, listener_id: int) -> List[model.Listening]: pass

    @abstractmethod
    async def get_all_artist(self) -> List[model.Artist]: pass

    @abstractmethod
    async def get_listening_per_months(self, artist_id: int) -> List[model.Listening]: pass
