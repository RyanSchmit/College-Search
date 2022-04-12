import csv

#input college you want to search
name = input('Enter college name: ')

#read csv, and split on "," the line
csv_file = csv.reader(open('collegevine.csv', "r"))


#loop through the csv list
for row in csv_file:
    if name == row[1]:
         print(row[0])

