'''Array 2D ตรวจสอบ'''
def main():
    '''Array 2D ตรวจสอบ'''
    grid = []
    for _ in range(5):
        row = list(map(int, input().split()))
        grid.append(row)

    ans_row = -1
    ans_col = -1

    for r in range(5):
        if sum(grid[r]) % 2:
            ans_row = r
            break

    for c in range(5):
        col_sum = sum(grid[r][c] for r in range(5))
        if col_sum % 2:
            ans_col = c
            break

    print(ans_row, ans_col)
main()
