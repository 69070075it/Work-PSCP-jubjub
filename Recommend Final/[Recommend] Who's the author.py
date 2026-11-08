'''[Recommend] Who's the author'''
def main():
    '''[Recommend] Who's the author'''
    wrote = {}
    while True:
        text = input()
        if text == 'END':
            break
        who, book = text.split(' ')
        if who not in wrote:
            wrote[who] = []
        if book not in wrote[who]:
            wrote[who].append(book)
    if not wrote:
        print('No Information')
    else:
        for who, book in wrote.items():
            print(f'{who}: {book}')
main()
