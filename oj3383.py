'''Difference'''
def main():
    '''Difference'''
    sum_n = int(input())
    sum_m = int(input())

    set_a = set()
    for _ in range(sum_n):
        set_a.add(int(input()))

    set_b = set()
    for _ in range(sum_m):
        set_b.add(int(input()))

    diff = set_a - set_b

    result = sorted(diff)

    print(*result)
main()
