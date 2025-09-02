from fastapi import UploadFile
from internal import interface, model
import io

class ArtistService(interface.IArtistService):
    def __init__(self, artist_repo: interface.IArtistRepo, storage: interface.IStorage):
        self.artist_repo = artist_repo
        self.storage = storage
    async def create_artist(
            self,
            account_id: int,
            avatar_file: UploadFile,
            name: str,
            description: str
    ) -> int:

        file_bytes = await avatar_file.read()
        file = io.BytesIO(file_bytes)

        upload_resp = self.storage.upload(file=file, name=avatar_file.filename)

        avatar_fid = upload_resp.fid

        artist_id = await self.artist_repo.create_artist(
            account_id,
            avatar_fid,
            name,
            description

        )
        return artist_id

    async def edit_name(self, artist_id: int, name: str) -> None: pass

    async def edit_avatar(self, artist_id: int, avatar_file: UploadFile) -> None: pass

    async def edit_description(self, artist_id: int, description: str) -> None: pass

    async def increment_artist_like(self, artist_id: int) -> None: pass

    async def decrement_artist_like(self, artist_id: int) -> None: pass

    async def add_listener(self, artist_id: int, listener_id: int) -> None: pass

    async def get_all_artist(self) -> List[model.Artist]: pass

    async def get_listening_count_per_months(self, artist_id: int) -> int: pass