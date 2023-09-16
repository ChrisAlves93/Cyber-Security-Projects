import random

uppercase_letters = 'ABCDEFGHIJKLMNEPQRSTUVWXYZ'
lowercase_letters = uppercase_letters.lower()
digits = '1234567890'
symbols = '!@#$%^&*()-_=+[]{}|;:,.<>/?~`±§°ºª¿®�'

upper, lower, nums, syms = True, True, True, True

all = ''

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 20
amount = 5

print(f'Welcome, these are your {amount} random generatored passwords\n')

for x in range(amount):
    password = ''.join(random.sample(all, length))
    print(password)