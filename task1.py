from datetime import datetime
from datetime import date

def calculate_age(born):
    today = date.today()
    birthday = datetime.strptime(born, "%d-%m-%Y")
    return today.year - birthday.year
result = calculate_age("15-01-1995")
print(result)