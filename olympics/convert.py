# This program was written by Ruben Boero

# The CSV files used in this program can be found on this site:
# https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

import csv

# source on how to write to a CSV file in py
# https://www.codingem.com/python-write-to-csv-file/

# source on how to write to mulitple files at once:
# https://stackoverflow.com/questions/4617034/how-can-i-open-multiple-files-using-with-open-in-python

dict_of_olympic_games = {}
dict_of_events = {}
dict_of_athletes = {}
with open('athlete_events.csv', 'r') as read_file:
    with open('olympic_games.csv', 'w') as olympic_games_file, open('events.csv', 'w') as events_file, \
        open('athletes.csv', 'w') as athletes_file:
        reader = csv.reader(read_file, delimiter=',')

        olympic_games_writer = csv.writer(olympic_games_file)
        events_writer = csv.writer(events_file)
        athletes_writer = csv.writer(athletes_file)

        next(reader) # skip the header line in the athlete_events.csv file

        for line in reader:
            athlete_ID = line[0]
            athlete_name = line[1]
            olympic_game = line[8]
            olympic_games_year = line[9]
            olympic_games_season = line[10]
            olympic_games_city = line[11]
            event_name = line[13]

            olympic_games_line = []
            events_line = []
            athletes_line = []

            # create olympic_games.csv
            if olympic_game not in dict_of_olympic_games:
                olympic_game_ID = len(dict_of_olympic_games) + 1
                dict_of_olympic_games[olympic_game] = olympic_game_ID

                olympic_games_line.append(olympic_game_ID)
                olympic_games_line.append(olympic_games_year)
                olympic_games_line.append(olympic_games_season)
                olympic_games_line.append(olympic_games_city)
                olympic_games_writer.writerow(olympic_games_line)

            # create events.csv
            if event_name not in dict_of_events:
                # following 2 lines of code taken from Jeff's olympics-convert file
                event_ID = len(dict_of_events) + 1
                dict_of_events[event_name] = event_ID

                events_line.append(event_ID)
                events_line.append(event_name)
                events_writer.writerow(events_line)

            # create athletes.csv
            if athlete_name not in dict_of_athletes:
                # set the ID of the current athlete to be true so that the athlete wont be added again
                dict_of_athletes[athlete_name] = athlete_ID
                # the ID is line[0] bc of the ID column in athlete_events.csv
                athletes_line.append(athlete_ID)
                athletes_line.append(athlete_name)
                athletes_writer.writerow(athletes_line)

dict_of_nocs = {}
# create the noc.csv
with open('noc_regions.csv', 'r') as read_file:
    with open('nocs.csv', 'w') as noc_file:
        reader = csv.reader(read_file, delimiter=',')
        noc_writer = csv.writer(noc_file)
        
        next(reader) # skip the header line in the csv file

        for line in reader:
            noc_line = []
            noc_abbreviation = line[0]
            noc_region = line[1]
            noc_ID = len(dict_of_nocs) + 1
            
            dict_of_nocs[noc_abbreviation] = noc_ID
            
            noc_line.append(noc_ID)
            noc_line.append(noc_abbreviation)
            noc_line.append(noc_region)
            noc_writer.writerow(noc_line)

dict_of_medals = {}
# create the medals csv file and medals dictionary
with open('medals.csv', 'w') as medals_file:
    # class of medal is the key, ID is stored
    dict_of_medals['NA'] = 1
    dict_of_medals['Bronze'] = 2
    dict_of_medals['Silver'] = 3
    dict_of_medals['Gold'] = 4
    medals_writer = csv.writer(medals_file)

    medals_line = ['1', 'NA']
    medals_writer.writerow(medals_line)
    medals_line = ['2', 'Bronze']
    medals_writer.writerow(medals_line)
    medals_line = ['3', 'Silver']
    medals_writer.writerow(medals_line)
    medals_line = ['4', 'Gold']
    medals_writer.writerow(medals_line)


# create the linking table
with open('athlete_events.csv') as original_data_file,\
        open('athletes_nocs_olympic_games_events_medals.csv', 'w') as write_file:
    
    reader = csv.reader(original_data_file)
    writer = csv.writer(write_file)

    next(reader)

    for line in reader:
        athlete_name = line[1]
        noc_abbrevation = line[7]
        olympic_game = line[8]
        olympic_games_year = line[9]
        olympic_games_season = line[10]
        olympic_games_city = line[11]
        event_name = line[13]
        medal_class = line[14]

        # athlete ID can be pulled directly from the athlete_events.csv file
        athlete_ID = line[0]
        # the noc_regions.csv file has SGP listed as the abbreviation for Singapore, I changed the noc_regions abbreviation
        # for Singapore to be SIN to match the athlete_events.csv. I have included a case for if this change is not made.
        if noc_abbrevation in dict_of_nocs:
            noc_ID = dict_of_nocs[noc_abbrevation]
        else:
            noc_ID = -1
        # get the rest of the IDs from the corresponding dictionaries
        olympic_game_ID = dict_of_olympic_games[olympic_game]
        event_ID = dict_of_events[event_name]
        medal_ID = dict_of_medals[medal_class]

        # write the line for the linking table
        writer.writerow([athlete_ID, noc_ID, olympic_game_ID, event_ID, medal_ID])

            

            
