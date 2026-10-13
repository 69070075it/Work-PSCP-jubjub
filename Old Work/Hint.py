'''Hint'''
def main():
    '''Hint'''
    aug1, one = input().split()
    aug2, two = input().split()
    aug3, three = input().split()
    one  = int(one)
    two = int(two)
    three = int(three)

    for i in range(10):
        if aug3 == '==' and not i == three:
            continue
        elif aug3 == '>=' and not i >= three:
            continue
        elif aug3 == '>' and not i > three:
            continue
        elif aug3 == '<' and not i < three:
            continue
        elif aug3 == '<=' and not i <= three:
            continue
        elif aug3 == '!=' and not i != three:
            continue
        for j in range(10):
            if aug2 == '==' and not j == two:
                continue
            elif aug2 == '>=' and not j >= two:
                continue
            elif aug2 == '>' and not j > two:
                continue
            elif aug2 == '<=' and not j <= two:
                continue
            elif aug2 == '<' and not j < two:
                continue
            elif aug2 == '!=' and not j != two:
                continue
            for k in range(10):
                if aug1 == '==' and not k == one:
                    print(f'{i}{j}{k}')
                    continue
                elif aug1 == '>=' and not k >= one:
                    print(f'{i}{j}{k}')
                    continue
                elif aug1 == '>' and not k > one:
                    print(f'{i}{j}{k}')
                    continue
                elif aug1 == '<' and not k < one:
                    print(f'{i}{j}{k}')
                    continue
                elif aug1 == '<=' and not k <= one:
                    print(f'{i}{j}{k}')
                    continue
                elif aug1 == '!=' and not k != one:
                    print(f'{i}{j}{k}')
main()
