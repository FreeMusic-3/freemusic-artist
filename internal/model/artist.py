from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Artist:
    id: int

    account_id: int
    avatar_fid: str
    name: str
    likes_count: int
    description: str

    @classmethod
    def serialize(cls, rows) -> list['Artist']:
        return [
            cls(
                id=row.id,
                account_id=row.account_id,
                avatar_fid=row.avatar_fid,
                name=row.name,
                likes_count=row.likes_count,
                description=row.description
            )
            for row in rows
        ]


@dataclass
class Listening:
    id: int

    listener_id: int
    artist_id: int
    created_at: datetime

    @classmethod
    def serialize(cls, rows) -> list['Listening']:
        return [
            cls(
                id=row.id,
                listener_id=row.listener_id,
                artist_id=row.artist_id,
                created_at=row.created_at,
            )
            for row in rows
        ]