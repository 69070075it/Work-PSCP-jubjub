'''BusStop I'''
def main():
    '''BusStop I'''
    p = int(input())
    n = int(input())

    stops = {}
    for _ in range(n):
        line = list(map(int, input().split()))
        stop_num = line[0]
        passenger = line[1:]
        stops[stop_num] = passenger

    bus = []
    total_drop = 0

    for cur_stop in range(1, n+1):
        new_bus = []
        for passen in bus:
            if passen == cur_stop:
                total_drop += 1
            else:
                new_bus.append(passen)
        bus = new_bus

        if cur_stop in stops:
            for target in stops[cur_stop]:
                if target > cur_stop and len(bus) < p:
                    bus.append(target)

    print(total_drop)
main()
