'''PickThemAgain'''
def main():
    '''PickThemAgain'''
    x = list(map(int, input().split()))
    y = x[::-1]
    total = 0
    for i in y:
        if not i%3 or not i%5:
            total += 1
            print(i)
    if not total:
        print('Nope')
main()
