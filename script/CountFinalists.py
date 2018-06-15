import csv
import re
import io
import collections

# A script to convert a CSV file into multiple markdown text files.
# Created by David Schirduan for the 200 Word RPG Challenge

# tracks all titles to make sure the same game isn't submitted twice by the same author

finalists = {}

with open('Choices.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:

        # Rows: timestamp name 1st 2nd 3rd 4th 5th
        
        first = row[2].lower().strip()
        second = row[3].lower().strip()
        third = row[4].lower().strip()
        fouth = row[5].lower().strip()
        fifth = row[6].lower().strip()

        if finalists.get(first) == None:
            finalists[first] = 0
        if finalists.get(second) == None:
            finalists[second] = 0
        if finalists.get(third) == None:
            finalists[third] = 0
        if finalists.get(fouth) == None:
            finalists[fouth] = 0
        if finalists.get(fifth) == None:
            finalists[fifth] = 0

        finalists[first] = finalists.get(first) + 5
        finalists[second] = finalists.get(second) + 4
        finalists[third] = finalists.get(third) + 3
        finalists[fouth] = finalists.get(fouth) + 2
        finalists[fifth] = finalists.get(fifth) + 1


od = collections.OrderedDict(sorted(finalists.items()))

for key, value in od.items():
    print(key, "~", value)

        



