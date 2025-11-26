# report.py




import fileparse
from porty.portfolio import Portfolio
from stock import Stock
import logging
import tableformat

log = logging.getLogger(__name__)


def read_portfolio(filename):
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float]
        )

    portfolio = [Stock(**d) for d in portdicts]
    log.info(f"type of portfolio: {type(portfolio)}")
    s = Portfolio()
    s.append(portfolio)
    return s


def read_prices(filename):
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report_data(portfolio, prices):
    rows = []
    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.price
        summary = (s.name, s.shares, current_price, change)
        rows.append(summary)
    return rows


def print_report(reportdata, formatter):
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt="txt"):
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(args):
    if len(args) != 4:
        raise SystemExit("Usage: %s portfile pricefile format" % args[0])
    portfolio_report(args[1], args[2], args[3])


if __name__ == "__main__":
    import sys

    main(sys.argv)
