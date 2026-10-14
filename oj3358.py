'''pig'''
def main():
    '''pig'''
    pair = int(input())
    weight = list(map(int, input().split()))

    max_weight = []

    for i in range(0, pair*2, 2):
        w1 = weight[i]
        w2 = weight[i+1]
        max_weight.append(max(w1, w2))

    total = sum(max_weight)

    if pair == 1:
        print(total)
    else:
        num = (' + '.join(str(w) for w in max_weight))
        print(f'{num} = {total}')
main()
