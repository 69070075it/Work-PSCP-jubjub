'''PSCP-P04'''
def main():
    '''PSCP-P04'''
    n, t = map(int, input().split())
    x = list(map(int, input().split()))
    total = 0
    ans = -1

    for i in range(n):
        total += x[i]
        if total >= t:
            ans = i + 1
            break
    print(ans)
main()
