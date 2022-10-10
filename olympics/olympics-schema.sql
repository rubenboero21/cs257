CREATE TABLE athletes (
    id SERIAL,
    name text
);

CREATE TABLE olympic_games (
    id SERIAL,
    year integer,
    season text,
    city text
);

CREATE TABLE events (
    id SERIAL,
    event text
);

CREATE TABLE nocs (
    id SERIAL,
    abbreviation char(3),
    region text
);

CREATE TABLE medals (
    id SERIAL,
    class text
);

CREATE TABLE athletes_nocs_olympic_games_events_medals (
    athlete_id integer,
    noc_id integer,
    olympic_game_id integer,
    event_id integer,
    medal_id integer
);