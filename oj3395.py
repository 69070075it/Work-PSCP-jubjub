'''เข้าเเถว'''
def main():
    '''เข้าเเถว'''
    n, _ = map(int, input().split())
    height = list(map(int, input().split()))
    cus = [int(x) - 1 for x in input().split()]

    max_front = [0] * n
    cur_max = 0
    for i in range(n):
        max_front[i] = cur_max
        if height[i] > cur_max:
            cur_max = height[i]

    for idx in cus:
        h = height[idx]
        highest = max_front[idx]

        if h > highest:
            print(0)
        else:
            print((highest - h) + 1)
main()
