'''ขายรถยนต์'''
def car():
    '''ขายรถยนต์'''
    n = int(input())

    v_list = []

    for i in range(n):
        data = input().split()
        v = int(data[1])
        v_list.append(v)

    unsell_count = 0
    max_v = -1

    for i in range(n-1, -1, -1):
        cur_v = v_list[i]

        if cur_v < max_v:
            unsell_count += 1
        else:
            max_v = cur_v

    print(unsell_count)
car()
