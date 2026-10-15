'''smart trash collector'''
def main():
    '''smart trash collector'''
    n_bin = int(input())
    total = 0
    outputs = []

    for _ in range(n_bin):
        plas, bot, glass = map(float, input().split())
        total = plas + bot + glass

        result = [f'{total:.1f}']

        if total > 50:
            result.append('Overloaded')
        if plas > 20:
            result.append('Check Type Plastic')
        if bot > 20:
            result.append('Check Type Can')
        if glass > 20:
            result.append('Check Type Glass')

        outputs.append(", ".join(result))

    print('\n'.join(outputs))
main()
