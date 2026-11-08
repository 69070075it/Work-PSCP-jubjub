'''[Recommend] 3nPlus1'''
def main():
    '''[Recommend] 3nPlus1'''
    total = []
    while True:
        num = int(input())
        if not num:
            break
        count = 1
        while num != 1:
            if not num % 2:
                num = num // 2
            else:
                num = (3*num) + 1
            count += 1
        total.append(count)
    for i in total:
        print(i)
main()
