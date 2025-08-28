from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Album:
    id: int

    artist_id: int
    cover_fid: str
    name: str
    description: str
    likes_count: int
    realised_at: datetime
    created_at: datetime


@dataclass
class Track:
    id: int

    track_fid: str
    album_id: int
    name: str
    duration: int
    listeners_count: int
    likes_count: int
    lyrics: str