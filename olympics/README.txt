I was not sure how to handle the data entries such as age, sex, team, etc. that could possibly change from 
games to games, so I chose to not inlude those items in my database.

In the noc_regions.csv file, I changed line 180 from 'SIN,Singapore,' to 'SGP,Singapore,' in order to match 
the athlete_events.csv NOC column. If this change is not made, all athletes from Singapore will be given an
NOC ID of -1. This causes some issues when searching within the database, but I have not tested extensively 
what the issues are.