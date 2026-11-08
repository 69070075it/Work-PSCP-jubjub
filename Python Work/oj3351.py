'''พูดจาภาษากระต่าย'''
def main():
    '''พูดจาภาษากระต่าย'''
    text = input().upper()
    n = len(text)

    if all(ch in 'IT' for ch in text):
        print(f'unknown {n}')
        return

    for i in range(n):
        ch = text[i]

        if ch not in 'RABIT':
            print(f'no {i}')
            return

        if ch == 'R':
            if i + 1 >= n or text[i+1] != 'A':
                print(f'no {i+1 if i+1 < n else i}')
                return

        if ch == 'A':
            if not i or text[i-1] not in 'RA':
                print(f'no {i}')
                return

        if ch == 'B':
            if i + 1 >= n or text[i+1] not in 'IT':
                print(f'no {i+1 if i+1 < n else i}')
                return

    max_a = 0
    cur_a = 0
    for ch in text:
        if ch == 'A':
            cur_a += 1
            max_a = max(max_a, cur_a)
        else:
            cur_a = 0

    print(f'yes {max_a}')
main()
