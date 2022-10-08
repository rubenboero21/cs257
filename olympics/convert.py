# This program was written by Ruben Boero

# The CSV files used in this program can be found on this site:
# https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

import csv

# source on how to write to a CSV file in py
# https://www.codingem.com/python-write-to-csv-file/

# source on how to write to mulitple files at once:
# https://stackoverflow.com/questions/4617034/how-can-i-open-multiple-files-using-with-open-in-python

with open('test.csv', 'r') as read_file:
    with open('olympic_games.csv', 'w') as olympic_games_file, open('events.csv', 'w') as events_file, open('athletes.csv', 'w') as athletes_file:
        reader = csv.reader(read_file, delimiter=',')

        olympic_games_writer = csv.writer(olympic_games_file)
        events_writer = csv.writer(events_file)
        athletes_writer = csv.writer(athletes_file)

        olympics_ID_counter = 1 # start at 1 to match the CSV 
        events_ID_counter = 1
        athletes_ID_counter = 1

        list_of_games = []
        list_of_events = []
        list_of_athletes = []

        next(reader) # skip the header line in the csv file

        for line in reader:
            # lists used to build each line before it is written to a file
            olympic_games_line = []
            events_line = []
            athletes_line = []

            # create olympic_games.csv
            # if the 'Games' col is not already in the list of games added, add the new game
            if line[8] not in list_of_games:
                olympic_games_line.append(str(olympics_ID_counter))
                olympic_games_line.append(line[9])
                olympic_games_line.append(line[10])
                olympic_games_line.append(line[11])

                olympic_games_writer.writerow(olympic_games_line)
                list_of_games.append(line[8])
                olympics_ID_counter += 1

            # create events.csv
            if line[13] not in list_of_events:
                events_line.append(str(events_ID_counter))
                events_line.append(line[13])

                events_writer.writerow(events_line)
                list_of_events.append(line[13])
                events_ID_counter += 1
            
            # create athletes.csv
            if line[1] not in list_of_athletes:
                athletes_line.append(str(athletes_ID_counter))
                athletes_line.append(line[1])

                athletes_writer.writerow(athletes_line)
                list_of_athletes.append(line[1])
                athletes_ID_counter += 1

# create the noc.csv
with open('noc_regions.csv', 'r') as read_file:
    with open('noc.csv', 'w') as noc_file:
        reader = csv.reader(read_file, delimiter=',')
        noc_writer = csv.writer(noc_file)
        noc_ID_counter = 1
        
        next(reader) # skip the header line in the csv file

        for line in reader:
            noc_line = []
            
            noc_line.append(str(noc_ID_counter))
            noc_line.append(line[0])
            noc_line.append(line[1])

            noc_writer.writerow(noc_line)
            noc_ID_counter += 1

# create the medals csv file
with open('medals.csv', 'w') as medals_file:
    medals_writer = csv.writer(medals_file)
    medals_line = ['1', 'N/A']
    medals_writer.writerow(medals_line)
    medals_line = ['2', 'bronze']
    medals_writer.writerow(medals_line)
    medals_line = ['3', 'silver']
    medals_writer.writerow(medals_line)
    medals_line = ['4', 'gold']
    medals_writer.writerow(medals_line)

# create the linking table
with open('olympic_games.csv', 'r') as olympic_games_read, open('events.csv', 'r') as events_read, open('athletes.csv', 'r') as athletes_read:
    with open('athletes_olympic_games_events_medals.csv', 'w') as write_file:
        pass