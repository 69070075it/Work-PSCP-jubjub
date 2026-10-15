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
        row = [direction[char][i] for char in inp]
        print(" ".join(row))

main()
