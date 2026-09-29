CREATE TABLE users (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    username VARCHAR(255)
);
INSERT INTO users (user_id, first_name, last_name, username)
VALUES ('12345', 'Bella', 'Hadid', 'bellahadid');
INSERT INTO users (user_id, first_name, last_name, username)
VALUES ('54321', 'Kylie', 'Jenner', 'kyliejenner');
INSERT INTO users (user_id, first_name, last_name, username)
VALUES ('23143', 'Harry', 'Styles', 'harrystyles');
INSERT INTO users (user_id, first_name, last_name, username)
VALUES ('45532', 'Nicki', 'Minaj', 'nickiminaj');
INSERT INTO users (user_id, first_name, last_name, username)
VALUES ('14532', 'Ariana', 'Grande', 'arianagrande');
INSERT INTO users (user_id, first_name, last_name, username)
VALUES ('22331', 'Lionel', 'Messi', 'lionelmessi');
INSERT INTO users (user_id, first_name, last_name, username)
VALUES ('55532', 'Kylian', 'Mbappe', 'kylianmbappe');
INSERT INTO users (user_id, first_name, last_name, username)
VALUES ('44351', 'Cristiano', 'Ronaldo', 'cristiano');
INSERT INTO users (user_id, first_name, last_name, username)
VALUES ('32411', 'Summer', 'Walker', 'summerwalker');
INSERT INTO users (user_id, first_name, last_name, username)
VALUES ('15443', 'SZA', '', 'sza');
CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    likes INT,
    caption TEXT,
    date_of_post DATETIME,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
INSERT INTO posts (post_id, likes, caption, date_of_post, user_id)
VALUES (
        '11111',
        990000,
        'fashion show',
        '2025-02-01 09:10:16',
        (
            SELECT user_id
            FROM users
            WHERE username = 'bellahadid'
        )
    );
INSERT INTO posts (post_id, likes, caption, date_of_post, user_id)
VALUES (
        '22222',
        3024560,
        'hi',
        '2026-08-25 05:10:19',
        (
            SELECT user_id
            FROM users
            WHERE username = 'kyliejenner'
        )
    );
INSERT INTO posts (post_id, likes, caption, date_of_post, user_id)
VALUES (
        '33333',
        450632,
        'New York, Day 2',
        '2026-09-18 10:15:18',
        (
            SELECT user_id
            FROM users
            WHERE username = 'harrystyles'
        )
    );
INSERT INTO posts (post_id, likes, caption, date_of_post, user_id)
VALUES (
        '44444',
        123953,
        'BARBZ',
        '2024-04-15 04:03:23',
        (
            SELECT user_id
            FROM users
            WHERE username = 'nickiminaj'
        )
    );
INSERT INTO posts (post_id, likes, caption, date_of_post, user_id)
VALUES (
        '55555',
        2304567,
        'in the studio',
        '2025-03-12 03:45:10',
        (
            SELECT user_id
            FROM users
            WHERE username = 'arianagrande'
        )
    );
INSERT INTO posts (post_id, likes, caption, date_of_post, user_id)
VALUES (
        '66666',
        1234321,
        'VAMOS',
        '2026-06-15 10:07:34',
        (
            SELECT user_id
            FROM users
            WHERE username = 'lionelmessi'
        )
    );
INSERT INTO posts (post_id, likes, caption, date_of_post, user_id)
VALUES (
        '77777',
        7654091,
        'ALLEZ LES BLEUS',
        '2026-06-13',
        (
            SELECT user_id
            FROM users
            WHERE username = 'kylianmbappe'
        )
    );
INSERT INTO posts (post_id, likes, caption, date_of_post, user_id)
VALUES (
        '88888',
        1250983,
        'SIUUU',
        '2026-06-20',
        (
            SELECT user_id
            FROM users
            WHERE username = 'cristiano'
        )
    );
INSERT INTO posts (post_id, likes, caption, date_of_post, user_id)
VALUES (
        '99999',
        30456,
        'Album out now',
        '2025-11-20',
        (
            SELECT user_id
            FROM users
            WHERE username = 'summerwalker'
        )
    );
INSERT INTO posts (post_id, likes, caption, date_of_post, user_id)
VALUES (
        '10101',
        2012345,
        'SOS',
        '2022-11-26',
        (
            SELECT user_id
            FROM users
            WHERE username = 'sza'
        )
    );