seconds = int(60)   #in a minute
minutes = int(60)   #in an hour
hours = int(24)     #in a day
days = int(365)     #in a year
print("There are " + str(seconds) + " in a minute.")
print("There are " + str(seconds * minutes) + " in a hour.")
print("There are " + str(hours * seconds * minutes) + " in a day.")
print("There are " + str(days * hours * seconds * minutes) + " in a year.")
