import datetime,time

n = datetime.date.today()
today = n.strftime("%d-%m-%Y")

f = open("Events.txt")
lines = f.readlines()

for line in lines:
    ls = line.split()
    if ls[0] == today:
        print " ".join(ls[2:len(ls)+1])
