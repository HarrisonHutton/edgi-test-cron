import csv

with open('phmsa_data.csv') as f:
    reader = csv.reader(f)
    for row in csv:
        print(row)