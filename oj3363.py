'''ไข้หวัดกระต่ายสายพันธุ์ใหม่'''
def main():
    '''ไข้หวัดกระต่ายสายพันธุ์ใหม่'''
    r, c = map(int, input().split())

    rab_r, rab_c = map(int, input().split())

    n_dead = int(input())

    grid = [[0] * c for _ in range(r)]

    risk = 0

    for _ in range(n_dead):
        dead_r, dead_c = map(int, input().split())

        for i in range(max(0, dead_r - 2), min(r, (dead_r + 2)+1)):
            for j in range(max(0, dead_c - 2), min(c, (dead_c + 2)+1)):
                dist = max(abs(i - dead_r), abs(j - dead_c))

                if not dist:
                    risk = 100
                elif dist == 1:
                    risk = 60
                elif dist == 2:
                    risk = 20

                if risk > grid[i][j]:
                    grid[i][j] = risk

    safe = 0
    for row in grid:
        for x in row:
            if not x:
                safe += 1

    print(safe)
    print(f'{grid[rab_r][rab_c]}%')
main()
