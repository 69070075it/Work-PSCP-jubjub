'''ไฟส่อง'''
def main():
    '''ไฟส่อง'''
    n = int(input())
    lit = [0] * 360

    for _ in range(n):
        a, b = map(int, input().split())
        if a < b:
            for deg in range(a, b):
                lit[deg] = 1
        else:
            for deg in range(a, 360):
                lit[deg] = 1
            for deg in range(0, b):
                lit[deg] = 1

    if all(lit):
        print(360)
        return

    lit2 = lit + lit
    max_len = 0
    curr_len = 0

    for val in lit2:
        if val == 1:
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len
        else:
            curr_len = 0

    print(min(max_len, 360))

main()
