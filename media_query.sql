SELECT users.username,
    posts.caption
FROM users
    JOIN posts ON users.user_id = posts.user_id
WHERE users.username = 'sza';