'''ตำบลกระสุนตก'''
def main():
    '''ตำบลกระสุนตก'''
    n = int(input())
    shots = []
    for _ in range(n):
        x, y, d = map(int, input().split())
        shots.append((x, y, d))

    for tx in range(1001):
        for ty in range(1001):
            match = True
            for x, y, d in shots:
                if (tx - x) ** 2 + (ty - y) ** 2 != d ** 2:
                    match = False
                    break
            if match:
                print(f"{tx} {ty}")
                return

main()
