import random
def hello_world():
    message = 'Hello World'
    print(message, random.random())

def get_total_interest(init_loan, interest_rate, num_yrs):
    rep_amount = init_loan * (interest_rate ** num_yrs)
    return rep_amount-init_loan

def greet_user(usr_name):
    message = 'Hello ' + usr_name
    print(message)

wl=['one','two','three','four','five']

def first_word(nlist):
    nlist.sort()
    return nlist[0]

def do_the_thing():
    two = 1 + 1
    print(two)

print(first_word(wl))

name1='Jane'
name2='Joe'
hello_world()
greet_user(name1)
greet_user(name2)

interest = get_total_interest(1000, 1.05, 10)
print(interest)


birthday_is_today = True
number_of_items = 10
price = 10.00

if birthday_is_today:
    price = price * 0.85
    print(price)
if number_of_items > 5:
    price = price * 0.9

print(price)


for number in [1, 2, 3, 4, 5]:
    print(number)

for character in 'foobar':
    print(character)

for i in range(10, -10, -2):
    print(i)


for i in range(10):
    print(f'Start loop with i == {i}')
    if i == 3:
        print('Break out')
        break
    if i < 2:
        print(f'Continue')
        continue
    print('End loop')

n = 3
i = 0
while i < n:
    print("£")
    i += 1


