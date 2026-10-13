'''กระต่ายน้อยรัก BUU'''
def main():
    '''กระต่ายน้อยรัก BUU'''
    x = input().strip()
    xyai = x.upper()
    lex = len(x)
    if 'BUU' in xyai:
        maxu = 0
        for i in range(lex):
            if xyai[i] == 'B':
                count = 0
                j = i + 1
                while j < lex and xyai[j] == 'U':
                    count += 1
                    j += 1
                if count > maxu:
                    maxu = count
        print(f'Yes {maxu}')
    elif 'B' in xyai:
        idx = xyai.find('B')
        result = x[:idx+1] + ('U' * (lex - idx - 1))
        print(result)
    else:
        pattern = 'BUU' * lex
        print(pattern[:lex])
main()
