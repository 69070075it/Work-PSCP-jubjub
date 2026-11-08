'''PickThem'''
import json as j
def main():
    '''PickThem'''
    n = input()

    load = j.loads(n)

    even = False
    for i in load:
        if not i % 2:
            print(i)
            even = True

    if not even:
        print('Nope')
main()
