# This program was written by Ruben Boero

# The CSV files used in this program can be found on this site:
# https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

import csv

# source on how to write to a CSV file in py
# https://www.codingem.com/python-write-to-csv-file/

# source on how to write to mulitple files at once:
# https://stackoverflow.com/questions/4617034/how-can-i-open-multiple-files-using-with-open-in-python

with open('athletes_events.csv', 'r') as read_file:
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
    medals_line = ['1', 'NA']
    medals_writer.writerow(medals_line)
    medals_line = ['2', 'Bronze']
    medals_writer.writerow(medals_line)
    medals_line = ['3', 'Silver']
    medals_writer.writerow(medals_line)
    medals_line = ['4', 'Gold']
    medals_writer.writerow(medals_line)

# create the linking table
# how can i split this line into mulitple lines?
with open('athletes_events.csv', 'r') as main_read, open('olympic_games.csv', 'r') as olympic_games_read, open('events.csv', 'r') \
    as events_read, open('athletes.csv', 'r') as athletes_read, open('noc.csv', 'r') as noc_read, open('medals.csv', 'r') \
    as medals_read:
    with open('athletes_noc_olympic_games_events_medals.csv', 'w') as write_file:
        main_reader = csv.reader(main_read, delimiter=',')
        olymic_games_reader = csv.reader(olympic_games_read, delimiter=',')
        events_reader = csv.reader(events_read, delimiter=',')
        athletes_reader = csv.reader(athletes_read, delimiter=',')
        noc_reader = csv.reader(noc_read, delimiter=',')
        medals_reader = csv.reader(medals_read, delimiter=',')

        writer = csv.writer(write_file)

        next(main_reader) # skip the header line in the csv file

        for line in main_reader:

            linking_line = []
            athlete_ID = line[0]
            noc_abbr = line[7]
            olympic_year = line[9]
            event = line[13]
            medal = line[14]

            linking_line.append(athlete_ID)
            
            for noc_line in noc_reader:
                if noc_line[1] == noc_abbr:
                    noc_ID = noc_line[0]
                    linking_line.append(noc_ID)
                    break

            for olympic_games_line in olymic_games_reader:
                if olympic_games_line[1] == olympic_year:
                    olympic_ID = olympic_games_line[0]
                    linking_line.append(olympic_ID)
                    break
            
            for events_line in events_reader:
                if events_line[1] == event:
                    event_ID = events_line[0]
                    linking_line.append(event_ID)
                    break
            
            for medals_line in medals_reader:
                if medals_line[1] == medal:
                    medal_ID = medals_line[0]
                    linking_line.append(medal_ID)
                    break
            
            writer.writerow(linking_line)
            
            # send the readers back to the top of the file to search for the next athlete's info
            noc_read.seek(0)
            olympic_games_read.seek(0)
            events_read.seek(0)
            medals_read.seek(0)
            
            
