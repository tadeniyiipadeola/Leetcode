import random
from turtle import goto

min =1
max =6
prev_roll=[]


def Roll(value):
    got = random.randint(min, max)
    while value != got:
        prev_roll.append(got)
        got = random.randint(min, max)
    return got

def print_prev_rolls():
    for i in range(len(prev_roll)):
        print(prev_roll[i])

ans = Roll(4)
print("the Answer is: ", ans)
print_prev_rolls()
print(*prev_roll)