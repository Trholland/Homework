import datetime as dt
todayDate = dt.datetime.now()
print(todayDate.strftime('%B'))

day = 'Sunday'

def greeting():
    name = input('Input name:')
    day = input('Input day:')
    print(f'Hello {name}! Happy {day}!')
    print(f'Hello {name}! Happy Sunday!')

x = 'Hello'
try:
    print(hello)
except NameError:
    print('Invalid Name!')