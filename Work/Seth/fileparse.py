# fileparse.py
#
# Exercise 3.3
# fileparse.py
import csv
from pathlib import Path

def parse_csv(filename: Path, types: list, delimiter: str =",", has_headers=True,  select=None, silence_errors=True) -> list[dict] :
    '''
    Parse a CSV file into a list of records
    '''
    indices = []
    with open(filename) as f:
        rows = csv.reader(f,delimiter=delimiter)
        

        # Read the file headers
        if has_headers:
            headers = next(rows)

            # If a column selector was given, find indices of the specified columns.
            # Also narrow the set of headers used for resulting dictionaries
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []

        records = []
        converted_row = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]
            for func , val in zip(types, row):
                try:
                    converted_row.append(func(val))
                except ValueError as e:
                    if not silence_errors:
                        print(e)

            # Make a dictionary
            if has_headers:
                record = dict(zip(headers, converted_row))
            else:
                record = converted_row
            records.append(record)

    return records
