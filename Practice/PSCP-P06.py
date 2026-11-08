'''PSCP-P06'''
def main():
    '''PSCP-P06'''
    n = int(input())
    x = list(map(int, input().split()))
    max_diff = -1
    max_day = 2

    for i in range(1, n):
        diff = abs(x[i] - x[i-1])
        if diff > max_diff:
            max_diff = diff
            max_day = i + 1

    print(f'{max_day} {max_diff}')
main()
