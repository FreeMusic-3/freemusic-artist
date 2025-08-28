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


@dataclass
class Listening:
    id: int

    listener_id: int
    artist_id: int
    created_at: datetime
