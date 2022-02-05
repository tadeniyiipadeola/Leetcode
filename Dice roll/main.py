import random

min =1
max =6



def Roll(value, tries):
    got = random.randint(min, max)
    while tries != 0:
        tries=-1
        if got == value:
            return got
    print(got)


ans = Roll(4, 10)
print("the Answer is: ", ans)