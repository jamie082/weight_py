#!/usr/bin/python3

from sys import argv

script, filename = argv

print("Opening the file...")
target = open(filename, 'a')

print("Enter weight to log to text file:", end=' ')
weight = input()

print(f"Your weight is {weight}.")

print("Enter date in MMDDYYYY format", end=' ')
date = input()

print(f"Date is {date}.")

# write weight to file

target.write(weight)
target.write("\t")
target.write(date)
target.write("\n")

print("And finally, we close it.")
target.close()
