# This program was written by Ruben Boero

# The CSV files used in this program can be found on this site:
# https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

import csv

# source on how to write to a CSV file in py
# https://www.codingem.com/python-write-to-csv-file/

# source on how to write to mulitple files at once:
# https://stackoverflow.com/questions/4617034/how-can-i-open-multiple-files-using-with-open-in-python

# is this nested with thing the right thing to do?
with open('test.csv', 'r') as read_file:
    with open('olympic_games.csv', 'w') as olympic_games_file, open('events.csv', 'w') as events_file:
        reader = csv.reader(read_file, delimiter=',')

        olympic_games_writer = csv.writer(olympic_games_file)
        events_writer = csv.writer(events_file)
        olympics_ID_counter = 1 # start at 1 to match the CSV 
        events_ID_counter = 1
        list_of_games = []
        list_of_events = []

        next(reader) # skip the header line in the csv file

        for line in reader:
            olympic_games_line = []
            events_line = []

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


