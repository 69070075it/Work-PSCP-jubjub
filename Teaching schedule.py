'''Teaching schedule'''
import math as m
def amin():
    '''Teaching schedule'''
    n =int(input())
    a = int(input())
    total = n*a
    h = m.floor(total/60)
    b = total - (h*60)
    if not n:
        print('No teaching')
    elif not a:
        print('No teaching')
    elif not b:
        print(f'{h} hours')
    elif not h:
        print(f'{b} minute')
    else:
        print(f'{h} hours {b} minute')
amin()
