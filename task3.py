def result(amount, months, percent):
    amount = float(input())
    months = float(input())
    percent = float(input())
    return (amount * ((percent / 12 / 100 + 1) ** months))
a = result(1000000, 6, 12)
print(a)