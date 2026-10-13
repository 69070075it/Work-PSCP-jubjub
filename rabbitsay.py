'''พูดจาภาษากระต่าย'''
def main():
    '''พูดจาภาษากระต่าย'''
    x = list(input().upper())
    lex = len(x)
    total_a = 0
    maxtotal_a = 0
    noid = 0
    if 'R' in x or 'A' in x or 'B' in x or 'I' in x or 'T' in x:
        if 'A' in x:
            for i in x:
                if i == 'A':
                    x[i]
                if x[i-1] == 'R':
                    total_a += 1
                    if x[i+1] == 'A':
                        total_a +=1
                        if total_a > maxtotal_a:
                            maxtotal_a = total_a
        print(maxtotal_a)
    else:
        print('no')
        for k in range(lex):
            for _ in x:
                if x[k] != 'R' or 'A' or 'B' or 'I' or 'T':
                    noid = k
        print(noid)
main()
