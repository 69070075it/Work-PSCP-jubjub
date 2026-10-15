'''FourDirections'''
def main():
    '''FourDirections'''
    direction = {
        'U': ['  *  ', ' *** ', '* * *', '  *  ', '  *  '],
        'D': ['  *  ', '  *  ', '* * *', ' *** ', '  *  '],
        'L': ['  *  ', ' *   ', '*****', ' *   ', '  *  '],
        'R': ['  *  ', '   * ', '*****', '   * ', '  *  ']
    }

    inp = input()

    for i in range(5):
        row_str = [direction[char][i] for char in inp]
        print(' '.join(row_str))

main()
