import random
from turtle import goto

min =1
max =6
prev_roll=[]


def Roll(value):
    if value > max or value < min:
        return("Error the value input is out of range")
    got = random.randint(min, max)
    while value != got:
        prev_roll.append(got)
        got = random.randint(min, max)
    return got

def print_prev_rolls():
    for i in range(len(prev_roll)):
        print(prev_roll[i])

ans = Roll(7)
print("the Answer is: ", ans)
print_prev_rolls()
print(*prev_roll)