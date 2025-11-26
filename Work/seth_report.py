# report.py
#
# Exercise 2.4

import csv
from pathlib import Path

import fileparse
from porty.portfolio import Portfolio
from stock import Stock

FILE_LOCATION = Path(
    "/Users/sitschner/SBP/training/practical-python/Work", "Data", "portfolio.csv"
)
PRICES_LOCATION = Path(
    "/Users/sitschner/SBP/training/practical-python/Work", "Data", "prices.csv"
)


def read_csv_file(filename: Path):
    contents = filename.read_text()
    return csv.reader(contents.splitlines())


def read_port(filename: Path) -> list[dict]:
    portfolio = []
    rows = read_csv_file(filename)
    headers = next(rows)
    for row in rows:
        portfolio.append(dict(zip(headers, row)))
    return portfolio


def read_portfolio(filename):
    with open(filename) as file:
        portdicts = fileparse.parse_csv(
            file, select=["name", "shares", "price"], types=[str, int, float]
        )

    portfolio = [Stock(d["name"], d["shares"], d["price"]) for d in portdicts]
    return Portfolio(portfolio)


def read_prices(filename: Path) -> dict:
    prices = {}
    rows = read_csv_file(filename)
    for row in rows:
        try:
            prices[row[0]] = row[1]
        except IndexError:
            next
    return prices


def changes(current_portfolio: dict, current_prices: dict) -> None:
    for stock in current_portfolio:
        stock["change"] = float(current_prices[stock["name"]]) - float(stock["price"])


# more dynamic
def print_report(headers: tuple, table: dict) -> None:
    cell_length = len(max(headers)) + 2
    cell_formatter = ">" + str(cell_length)
    separator = "_" * cell_length
    separator = separator + " "

    for header in headers:
        print(f"{header:^9s}", end="")
    print()
    print(f"{separator * len(headers):^8s}")
    for stock in table:
        price = f"${float(stock['price']):.2f}"
        print(
            f"{stock['name']:^9s} {stock['shares']:^9s} {price} {stock['change']:^9.2f}"
        )


def main(argv: list):
    current_portfolio = read_portfolio(Path(argv[1]))
    current_prices = read_prices(argv[2])
    headers = ("Name", "Shares", "Price", "Change")
    changes(current_portfolio=current_portfolio, current_prices=current_prices)
    print_report(headers, current_portfolio)


if __name__ == "__main__":
    import sys

    main(sys.argv)
