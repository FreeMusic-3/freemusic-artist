from abc import abstractmethod
from datetime import datetime
from typing import Protocol
from fastapi import UploadFile
from internal import model


class IAlbumController(Protocol):
    @abstractmethod
    async def create_album(
            self,
            artist_id: int,
            cover_file: UploadFile,
            name: str,
            description: str,
            realised_at: datetime,
    ) -> int: pass

    @abstractmethod
    async def increment_album_like(self, album_id: int) -> None: pass

    @abstractmethod
    async def decrement_album_like(self, album_id: int) -> None: pass

    @abstractmethod
    async def create_track(
            self,
            track_file: UploadFile,
            album_id: int,
            name: str,
            lyrics: str,
    ) -> int: pass

    @abstractmethod
    async def increment_track_like(self, track_id: int) -> None: pass

    @abstractmethod
    async def decrement_track_like(self, track_id: int) -> None: pass

    @abstractmethod
    async def increment_track_listening(self, track_id: int) -> None: pass


class IAlbumService(Protocol):
    @abstractmethod
    async def create_album(
            self,
            artist_id: int,
            cover_file: UploadFile,
            name: str,
            description: str,
            realised_at: datetime,
    ) -> int: pass

    @abstractmethod
    async def increment_album_like(self, album_id: int) -> None: pass

    @abstractmethod
    async def decrement_album_like(self, album_id: int) -> None: pass

    @abstractmethod
    async def create_track(
            self,
            track_file: UploadFile,
            album_id: int,
            name: str,
            lyrics: str,
            duration: int,
    ) -> int: pass

    @abstractmethod
    async def increment_track_like(self, track_id: int) -> None: pass

    @abstractmethod
    async def decrement_track_like(self, track_id: int) -> None: pass

    @abstractmethod
    async def increment_track_listening(self, track_id: int) -> None: pass


class IAlbumRepo(Protocol):
    @abstractmethod
    async def create_album(
            self,
            artist_id: int,
            cover_fid: str,
            name: str,
            description: str,
            realised_at: datetime,
    ) -> int: pass

    @abstractmethod
    async def increment_album_like(self, album_id: int) -> None: pass

    @abstractmethod
    async def decrement_album_like(self, album_id: int) -> None: pass

    @abstractmethod
    async def create_track(
            self,
            track_fid: str,
            album_id: int,
            name: str,
            lyrics: str,
            duration: int,
    ) -> int: pass

    @abstractmethod
    async def increment_track_like(self, track_id: int) -> None: pass

    @abstractmethod
    async def decrement_track_like(self, track_id: int) -> None: pass

    @abstractmethod
    async def increment_track_listening(self, track_id: int) -> None: pass