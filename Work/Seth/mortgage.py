# mortgage.py
#
# Exercise 1.7
START_MONTH = 61
END_MONTH = 108
RATE = 0.05
EXTRA_PAYMENT = 1000
PAYMENT = 2684.11
month = 0
principal = 500000.0
total_paid = 0.0

while principal > 0:
    total_payment = PAYMENT
    if START_MONTH<= month <= END_MONTH:
        total_payment = PAYMENT + EXTRA_PAYMENT
    principal = principal * (1+RATE/12) - total_payment
    total_paid = total_paid + total_payment
    month = month + 1 

    print(f'Month: {month:<10}  Total paid: {total_paid:10.2f}    Remaining: {principal:10.2f}')
    if principal < 0:
        over_pay = PAYMENT + principal
        print(f"last month payment only {over_pay:0.2f}")

