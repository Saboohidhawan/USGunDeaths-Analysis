import csv
with open('guns.csv', 'r') as f:
    data = list(csv.reader(f))
headers = data[0]
data = data[1:]
year_counts={}
years = [row[1] for row in data]   
for year in years:
    if year in year_counts:
        year_counts[year] += 1
    else:
        year_counts[year] =1
year_counts

import datetime
dates = [datetime.datetime(year = int(row[1]), month = int(row[2]), day = 1) for row in data]
date_counts={}
for date in dates:
    if date in date_counts:
        date_counts[date] += 1
    else:
        date_counts[date] = 1
        
sex_counts={}
gender = [row[5] for row in data] 
for item in gender:
    if item in sex_counts:
        sex_counts[item] += 1
    else:
        sex_counts[item] =1
sex_counts

race_counts={}
race = [row[7] for row in data]
for item in race:
    if item in race_counts:
        race_counts[item] += 1
    else:
        race_counts[item] =1
race_counts

census = list(csv.reader(open('census.csv', 'r')))

mapping = {
    "Asian/Pacific Islander": 15834141,
    "Native American/Native Alaskan": 3739506,
    "Black": 40250635,
    "Hispanic": 44618105,
    "White": 197318956
}

race_per_hundredk = {}
for key, value in race_counts.items():
    race_per_hundredk[key] = (value/mapping[key])*100000
race_per_hundredk
    
intents =[row[3] for row in data]
races = [row[7] for row in data]
homicide_race_counts = {}
for i,race in enumerate(races):
    if intents[i] =="Homicide":
        if race not in homicide_race_counts:
            homicide_race_counts[race] = 1
        else:
            homicide_race_counts[race] += 1
homicide_race_counts

race_per_hundredk = {}
for key,value in homicide_race_counts.items():
    race_per_hundredk[key] = (value/mapping[key])*100000
race_per_hundredk
