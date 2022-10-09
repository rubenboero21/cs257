SELECT region
FROM noc
ORDER BY abbreviation ASC;

SELECT DISTINCT athletes.name
FROM athletes, noc, athletes_noc_olympic_games_events_medals
WHERE athletes.id = athletes_noc_olympic_games_events_medals.athlete_id
AND noc.id = athletes_noc_olympic_games_events_medals.noc_id
AND noc.abbreviation = 'JAM'
ORDER BY name ASC;

SELECT athletes.name, events.event, olympic_games.season, olympic_games.year, medals.class
FROM athletes, events, olympic_games, medals, athletes_noc_olympic_games_events_medals
WHERE athletes.name LIKE '%Greg% %Louganis%'
AND athletes.id = athletes_noc_olympic_games_events_medals.athlete_id
AND events.id = athletes_noc_olympic_games_events_medals.event_id
AND olympic_games.id = athletes_noc_olympic_games_events_medals.olympic_game_id
AND medals.id = athletes_noc_olympic_games_events_medals.medal_id
AND medals.class != 'NA'
ORDER BY year ASC;

SELECT noc.abbreviation, COUNT(medals.class)
FROM noc, medals, athletes_noc_olympic_games_events_medals
WHERE medals.id = athletes_noc_olympic_games_events_medals.medal_id
AND noc.id = athletes_noc_olympic_games_events_medals.noc_id
AND medals.class = 'Gold'
GROUP BY noc.abbreviation
ORDER BY COUNT(medals.class) DESC, noc.abbreviation;