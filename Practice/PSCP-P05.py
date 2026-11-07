'''PSCP-P05'''
def main():
    '''PSCP-P05'''
    n = int(input())
    x = list(map(int, input().split()))
    mid = sum(x) / n
    result = 0
    for i in x:
        if i > mid:
            result += 1
    print(f'{mid:.2f}')
    print(result)
main()
