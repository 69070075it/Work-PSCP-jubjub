'''LastStand'''
import json as j
def main():
    '''LastStand'''
    n = input()
    y = j.loads(n)
    for i in y:
        print(str(i)[-1])
main()
