'''ลอดสะพาน'''
def main():
    '''ลอดสะพาน'''
    line1 = input().split()
    length = int(line1[0])
    num_bridge = int(line1[1])

    bridge = []
    for _ in range(num_bridge):
        a_i, b_i = map(int, input().split())
        bridge.append((a_i, b_i))

    max_count = 0

    for i in range(length):
        point = i + 0.5
        count = 0
        for start, end in bridge:
            if start < point < end:
                count += 1
        if count > max_count:
            max_count = count

    print(max_count)
main()
