from lxml.html.builder import SELECT
from internal import interface, model
from .sql_query import *


class ArtistRepo(interface.IArtistRepo):
    def __init__(self, db: interface.IDB):
        self.db = db

    async def create_artist(
            self,
            account_id: int,
            avatar_fid: str,
            name: str,
            description: str
    ) -> int:
        args = {
            "account_id": account_id,
            "avatar_fid": avatar_fid,
            "name": name,
            "description": description,
        }
        artist_id = await self.db.insert(create_artist, args)
        return artist_id

    async def edit_name(self, artist_id: int, name: str) -> None:
        args = {
            "artist_id": artist_id,
            "name": name
        }
        await self.db.update(edit_name, args)

    async def edit_avatar(self, artist_id: int, avatar_fid: str) -> None:
        args = {
            "artist_id": artist_id,
            "avatar_fid": avatar_fid
        }
        await self.db.update(edit_avatar, args)

    async def edit_description(self, artist_id: int, description: str) -> None:
        args = {
            "artist_id": artist_id,
            "description": description
        }
        await self.db.update(edit_description, args)

    async def increment_artist_like(self, artist_id: int) -> None:
        args = {
            "artist_id": artist_id
        }
        await self.db.update(increment_artist_like, args)

    async def decrement_artist_like(self, artist_id: int) -> None:
        args = {
            "artist_id": artist_id
        }
        await self.db.update(decrement_artist_like, args)

    async def add_listener(self, artist_id: int, listener_id: int) -> None:
        args = {
            "artist_id": artist_id,
            "listener_id": listener_id
        }
        await self.db.insert(add_listener, args)

    async def get_listener(self, artist_id: int, listener_id: int) -> List[model.Listening]:
        args = {
            "artist_id": artist_id,
            "listener_id": listener_id
        }
        rows = await self.db.select(get_listener, args)
        result = model.Listening.serialize(rows) if rows else []
        return result

    async def get_all_artist(self) -> List[model.Artist]:
        rows = await self.db.select(get_all_artist, {})
        result = model.Artist.serialize(rows) if rows else []
        return result

    async def get_listening_per_months(self, artist_id: int) -> List[model.Listening]:
        args = {
            "artist_id": artist_id,
        }
        rows = await self.db.select(get_listenings_per_months, args)
        result = model.Listening.serialize(rows) if rows else []
        return result