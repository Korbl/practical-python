# pcost.py
#
# Exercise 1.27
from pathlib import Path
import csv

FILE_LOCATION = Path('/Users/sitschner/SBP/training/practical-python/Work', 'Data', 'portfolio.csv')


def read_csv_file(filename: Path):
   contents = filename.read_text()
   return csv.reader(contents.splitlines())


def portfolio(filename: Path) -> float:
    total_cost = 0.00
    rows = read_csv_file(filename)
    headers = next(rows)
    for row_number, row in enumerate(rows,start=1):
        record = dict(zip(headers,row))
        try:
            total_cost += int(record['shares']) * float(record['price'])
        except ValueError:
            print(f"Couldn't parse row number: {row_number}  row: {row}")
    return total_cost

costs = portfolio(FILE_LOCATION)
print(f"Total cost is {costs:0.2f}")