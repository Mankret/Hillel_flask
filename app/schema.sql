

CREATE TABLE IF NOT EXISTS tracks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  artist TEXT NOT NULL,
  genre TEXT NOT NULL,
  length INTEGER NOT NULL
);


INSERT INTO tracks (
    title,
    artist,
    genre,
    length
)
VALUES
    (
        'The Son of Flynn',
        'Daft Punk',
        'electronic',
         95
    ),
    (
        'Terminus (Where Death is Most Alive)',
        'Dark Tranquillity',
        'Melodic death metal',
         254
    ),
    (
        'Meds',
        'Placebo',
        'Alternative rock',
         215
    ),
    (
        'THE DEATH OF PEACE OF MIND',
        'BAD OMENS ',
        'Metal core',
         240
    ),
    (
        'Zeit',
        'Rammstein',
        'industrial metal',
         371
    ),
    (
        'Paris',
        'Else',
        'electronic',
         197
    ),
    (
        'I Hate Everything About You',
        'Three Days Grace',
        'alternative metal',
         204
    ),
    (
        'Nightcall',
        'Kavinsky',
        'electronic',
         250
    ),
    (
        'Free Party',
        'Paul Sabin',
        'electronic',
         318
    ),
    (
        'Gangsta`s Paradise',
        'Coolio',
        'West Coast hip hop',
         204
    ),
    (
        'Mein Herz Brennt',
        'Rammstein',
        'industrial metal',
         304
    ),
    (
        'Psychosocial',
        'Slipknot',
        'Nu metal',
         301
    ),
    (
        'Killpop',
        'Slipknot',
        'Nu metal',
         243
    ),
    (
        'Joker',
        'Dax',
        'hip hop',
         262
    ),
    (
        'Breaking the habit',
        'Linkin Park',
        'alternative metal',
         191
    ),
    (
        'Gotham',
        'Dax',
        'hip hop',
         188
    ),
    (
        'Your Numbers Up',
        'Ice Nine Kills',
        'metalcore',
         159
    ),
    (
        'Stabbing In The Dark',
        'Ice Nine Kills',
        'metalcore',
         261
    ),
    (
        'Times of Yore',
        'In Vain',
        'Progressive death metal',
         432
    );