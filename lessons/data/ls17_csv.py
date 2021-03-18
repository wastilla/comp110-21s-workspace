"""Example reading CSV files. """

from csv import DictReader

file_handle = open("lessons/data/csv practice.csv", "r", encoding="utf8")
csv_reader = DictReader(file_handle)

#A "table" can be modeled as a lisy of rows where a row is a dictionary with the column title as the key
table: list[dict[str, str]] = []

#Add each row of data to our table
for row in csv_reader:
    table.append(row)

#When were done reading / working with a file, we should close it!
file_handle.close()

print(table)