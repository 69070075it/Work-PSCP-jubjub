'''เเซงรอบ'''
def main():
    '''เเซงรอบ'''
    n, k = map(int, input().split())
    times = []

    for _ in range(n):
        times.append(int(input()))

    s_min = min(times)
    winner = k * s_min

    count = 0
    for s_i in times:
        if (k-1) * s_i < winner:
            count += 1

    print(count)
main()
