create_artist_table = """
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    account_id INT NOT NULL,
    avatar_fid TEXT,
    name TEXT NOT NULL,
    likes_count INT DEFAULT 0,
    description TEXT
);
"""
create_album_table = """
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    artist_id INT NOT NULL,
    cover_fid TEXT,
    name TEXT NOT NULL,
    description TEXT,
    likes_count INT DEFAULT 0,
    realised_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT NOW()
);
"""
create_track_table = """
CREATE TABLE tracks (
    id SERIAL PRIMARY KEY,
    track_fid TEXT NOT NULL,
    album_id INT NOT NULL,
    name TEXT NOT NULL,
    duration INT NOT NULL,
    listeners_count INT DEFAULT 0,
    likes_count INT DEFAULT 0,
    lyrics TEXT
);
"""
create_listening_table = """
CREATE TABLE listenings (
    id SERIAL PRIMARY KEY,
    listener_id INT NOT NULL,
    artist_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
"""

