SELECT region
FROM nocs
ORDER BY abbreviation ASC;

SELECT DISTINCT athletes.name
FROM athletes, nocs, athletes_nocs_olympic_games_events_sports_medals
WHERE athletes.id = athletes_nocs_olympic_games_events_sports_medals.athlete_id
AND nocs.id = athletes_nocs_olympic_games_events_sports_medals.noc_id
AND nocs.abbreviation = 'JAM'
ORDER BY name ASC;

SELECT athletes.name, events.event, olympic_games.season, olympic_games.year, medals.class
FROM athletes, events, olympic_games, medals, athletes_nocs_olympic_games_events_sports_medals
WHERE athletes.name ILIKE '%Greg% %Louganis%'
AND athletes.id = athletes_nocs_olympic_games_events_sports_medals.athlete_id
AND events.id = athletes_nocs_olympic_games_events_sports_medals.event_id
AND olympic_games.id = athletes_nocs_olympic_games_events_sports_medals.olympic_game_id
AND medals.id = athletes_nocs_olympic_games_events_sports_medals.medal_id
AND medals.class != 'NA'
ORDER BY olympic_games.year ASC;

SELECT nocs.abbreviation, COUNT(medals.class)
FROM nocs, medals, athletes_nocs_olympic_games_events_sports_medals
WHERE medals.id = athletes_nocs_olympic_games_events_sports_medals.medal_id
AND nocs.id = athletes_nocs_olympic_games_events_sports_medals.noc_id
AND medals.class = 'Gold'
GROUP BY nocs.abbreviation
ORDER BY COUNT(medals.class) DESC, nocs.abbreviation;