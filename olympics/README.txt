I was not sure how to handle the data entries such as age, sex, team, etc. that could possibly change from 
games to games, so I chose to not include those items in my database.

In the noc_regions.csv file, I changed line 180 from 'SIN,Singapore,' to 'SGP,Singapore,' in order to match 
the athlete_events.csv NOC column. If this change is not made, all athletes from Singapore will be given an
NOC ID of -1. This causes some issues when searching within the database, but I have not tested extensively 
what the issues are.

Sources used with sql queries:
Group by:
	https://www.w3schools.com/sql/sql_groupby.asp#:~:text=The%
	20SQL%20GROUP%20BY%20Statement,by%20one%20or%20more%20columns

Distinct:
	https://www.w3schools.com/sql/sql_distinct.asp#:~:text=The%20
	SQL%20SELECT%20DISTINCT%20Statement,the%20different%20(distinct)%20values

Count:
	https://learnsql.com/blog/group-by-in-sql/