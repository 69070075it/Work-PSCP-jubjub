'''Day08-0_02-Backward'''
def main():
    '''Day08-0_02-Backward'''
    i = []
    while True:
        x = input()
        if x == 'NULL':
            break
        i.append(x)

    for last in i[::-1]:
        print(last)

main()
