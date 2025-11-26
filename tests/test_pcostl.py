from porty.pcost import portfolio_cost
import pytest
from pathlib import Path
import csv

FILE_LOCATION = Path('does_not_exist.csv')
FILE_TEST = Path('/Users/sitschner/SBP/training/practical-python/Work', 'test_data', 'test_portfolio.csv')

def test_read_from_file(mocker):
    lines = FILE_TEST.read_text()
    mocker.patch(
        "pcost.read_csv_file",
        return_value=csv.reader(lines.splitlines())
    )   
    costs = portfolio_cost(FILE_LOCATION)

    assert costs == 58.00
    