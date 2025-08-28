create_artist_table = """
CREATE TABLE artist (
    id SERIAL PRIMARY KEY,
    account_id INT NOT NULL,
    avatar_fid TEXT,
    name TEXT NOT NULL,
    likes_count INT DEFAULT 0,
    description TEXT
);
"""
create_album_table = """
CREATE TABLE album (
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
CREATE TABLE track (
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
CREATE TABLE listening (
    listener_id INT NOT NULL,
    artist_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (listener_id, artist_id, created_at)
);
"""
