# Lab 1: Representing Data
# Author Anna Lozenko

# write a program to read in the data contained in the data.csv file and output each line as a list.
import csv
file = "data.csv"
with open(file, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for row in reader:
        print(row)

# What data type is each line that is output?
# Each line is a list data type.

# Modify the program to deal with the header line separately

with open(file, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0 # line counter
    for row in reader:
        if linecount == 0: # header line
            header = row # store header
            print(f"{header}\n----------------------")
        else:
            print(f"{linecount}: {row}")
        linecount += 1

# Modify the program to calculate the average age

with open(file, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0 # line counter
    total_age = 0 # total age accumulator
    for row in reader:
        if linecount == 0:
            pass # skip header
        else:
            total_age += int(row[1]) # age is the second column, convert to int
        linecount += 1
    average_age = total_age / (linecount - 1) # exclude header from count
    print(f"\nAverage Age: {average_age:.2f}")