'''cave explorer'''
def main():
    '''cave explorer'''
    n = int(input())
    cave = list(map(int, input().split()))
    cmd = input()

    pos = cave.index(1)
    trea = cave.index(2)

    cave[pos] = 0

    for i in cmd:
        if i == 'R':
            if pos < n-1:
                pos += 1
        elif i == 'L':
            if pos > 0:
                pos -= 1

        if pos == trea:
            break

    cave[pos] = 1

    print(*cave)
main()
