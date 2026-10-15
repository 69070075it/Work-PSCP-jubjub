'''array ฮาเฮ'''
def main():
    '''array ฮาเฮ'''
    number = []
    for i in range(1, 4):
        val = int(input())
        number.append(val)
        print(f'Input number {i} stored.')

    while True:
        choice = int(input())

        if not choice:
            break
        if choice == 1:
            print('Original order:', *number)
        elif choice == 2:
            mark = sorted(number, reverse=True)
            print('Descending order:', *mark)
        elif choice == 3:
            less = sorted(number)
            print('Ascending order:', *less)
main()
