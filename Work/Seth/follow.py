# follow.py
import os
import time

stocks = ['GOOG', 'APPL', 'IBM']

def follow(filename):
    f = open(filename)
    f.seek(0, os.SEEK_END) 
    while True:
        line = f.readline()
        if line == "":
            time.sleep(0.1)
            continue
        yield line


# for line in follow('Data/stocklog.csv'):
#     #print(line, end="")
#     fields = line.split(',')
#     name = fields[0].strip('"')
#     price = float(fields[1])
#     change = float(fields[4])
#     if name in stocks:
#         if change < 0:
#             print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

