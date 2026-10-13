'''ตั๋วหนังสุดป่วน'''
def main():
    '''ตั๋วหนังสุดป่วน'''
    n = int(input())
    while n > 0:
        x, y = map(int, input().split())
        if x < 15:
            print(-1)
            continue
        if y > n:
            print(-2)
            continue
        if 15 <= x <= 22:
            price = 120
        elif x >= 60:
            price = 75
        else:
            price = 150
        total = price * y
        n -= y
        print(f'{total} {n}')
main()
