from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

def print_hi(name):
    print(f'Hi, {name}')
    theDate = datetime.now()
    print('Today is', theDate.strftime("%x"))

if __name__ == '__main__':
    print_hi('yo')
    calculate_salary()
    get_employees()
