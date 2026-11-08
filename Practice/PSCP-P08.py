'''PSCP-P08'''
def main():
    '''PSCP-P08'''
    n = int(input())
    tt_win = 0
    tt_draw = 0
    tt_lose = 0
    for _ in range(n):
        result = input()
        if result == 'WIN':
            tt_win += 1
        elif result == 'LOSE':
            tt_lose += 1
        elif result == 'DRAW':
            tt_draw += 1
    total = (tt_win*3) + (tt_draw*1) + (tt_lose*0)
    print(f'{tt_win} {tt_draw} {tt_lose}')
    print(total)
main()
