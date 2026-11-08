'''PSCP-P11'''
def main():
    '''PSCP-P11'''
    f1, f2 = map(int, input().split())
    if f1 > 0:
        book_1 = set(input().split())
    else:
        book_1 = set()
    if f2 > 0:
        book_2 = set(input().split())
    else:
        book_2 = set()
    pair = book_1 & book_2
    print(len(pair))
main()
