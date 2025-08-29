create_artist = """
INSERT INTO artists (account_id, avatar_fid, name, description)
VALUES (:account_id, :avatar_fid, :name, :description)
RETURNING id;
"""

edit_name = """
UPDATE artists
SET name = :name
WHERE id = :artist_id
"""

edit_avatar = """
UPDATE artists
SET avatar_fid = :avatar_fid
WHERE id = :artist_id
"""

edit_description = """
UPDATE artists
SET description = :description
WHERE id = :artist_id
"""

increment_artist_like = """
UPDATE artists
SET likes_count = likes_count + 1
WHERE id = :artist_id
"""

decrement_artist_like = """
UPDATE artists
SET likes_count = likes_count - 1
WHERE id = :artist_id
"""

add_listener = """
INSERT INTO listenings (artist_id, listener_id)
VALUES (:artist_id, :listener_id)
RETURNING id;
"""

get_listener = """
SELECT * FROM listenings
WHERE artist_id = :artist_id AND listener_id = :listener_id
"""

get_all_artist = """
SELECT * FROM artists
"""

get_listenings_per_months = """
SELECT * FROM listenings
WHERE created_at >= date_trunc('month', CURRENT_DATE)
AND created_at < (date_trunc('month', CURRENT_DATE) + interval '1 month');
"""